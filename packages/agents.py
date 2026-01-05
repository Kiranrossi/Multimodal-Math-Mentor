from pydantic import BaseModel, Field
from typing import List, Optional
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.agents import create_tool_calling_agent, AgentExecutor
import os
import packages.rag as rag
import packages.calculator as calculator

class MathProblem(BaseModel):
    problem_text: str = Field(description="The clear, cleaned text of the math problem.")
    topic: str = Field(description="The mathematical topic (e.g., Algebra, Calculus, Geometry, Probability, Linear Algebra).")
    variables: List[str] = Field(description="List of variables involved (e.g., ['x', 'y']).")
    constraints: List[str] = Field(description="Any constraints mentions (e.g., 'x > 0').")
    needs_clarification: bool = Field(description="True if the problem is ambiguous or incomplete, else False.")

def get_parser_agent():
    """
    Returns a chain that accepts a dictionary {"raw_input": str} 
    and returns a MathProblem object.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found.")
    
    # Using Llama-3.3-70b-versatile (Latest)
    llm = ChatGroq(
        model="llama-3.1-8b-instant", # Switched to 8b to avoid Rate Limits on 70b
        api_key=api_key,
        temperature=0.0
    )
    
    parser = JsonOutputParser(pydantic_object=MathProblem)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert Math Parser. specificy in extracting structured data from raw math questions.\n"
                   "Clean up the text, identify the topic (Algebra, Calculus, Linear Algebra, Probability, or Basic Arithmetic), variables, and constraints.\n"
                   "If the input is gibberish or missing critical info, set needs_clarification=True.\n"
                   "\n{format_instructions}"),
        ("human", "Raw Input: {raw_input}")
    ])
    
    # We use RunnablePassthrough to inject the format_instructions into the prompt
    chain = (
        RunnablePassthrough.assign(
            format_instructions=lambda _: parser.get_format_instructions()
        )
        | prompt 
        | llm 
        | parser
    )
    
    return chain

def get_solver_agent():
    """
    Returns a chain that accepts {"structured_problem": MathProblem} 
    and returns a step-by-step solution string.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found.")
    
    # Use a smart model for solving
    # Using llama-3.1-8b-instant for speed and to avoid Rate Limits
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=api_key,
        temperature=0.1
    )
    
    # Tools 
    tools = [calculator.calculate]
    
    # Prompt for Agent (Must include scratchpad)
    # We use a chat prompt with system instructions
    system_message = """You are an expert JEE Math Tutor.
    Your goal is to help a student understand the concepts deeply, not just get the answer.
    
    Context (Formulas/Rules):
    {context}
    
    Problem Details:
    Topic: {topic}
    Variables: {variables}
    
    Instructions:
    1. **Structure your response exactly as follows**:
       - `### Understanding the Problem`: A brief conceptual intro.
       - `### Step 1: Identify Key Information`: List given values and what we need to find.
       - `### Step 2: Apply the Concept/Formula`: State the formula/rule explicitly and substitute values.
       - `### Step 3: Solve Calculation`: Show the math clearly.
       - `### Why This Works`: A subtle explanation of the logic (e.g., "Probability works because...").
       - `### Conclusion`: A final summary sentence.
       - `### Final Answer`: The clear, boxed result (e.g., **x = 5**).
    2. **Be Extremely Didactic**: Imagine you are writing a textbook explanation.
    3. **Go Deep**: Don't just say "Add 2+2". Say "Since we have 2 apples and add 2 more, we sum them...".
    4. **Formatting**: PLAIN TEXT ONLY.
       - **DO NOT usage LaTeX**.
       - **DO NOT use $ dollar signs**.
       - Write fractions as `3/8` or `1/2`.
       - Write squares as `x^2`.
       - Write multiplication as `*` or `x`.
       - Keep it readable and simple.
    """
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_message),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    
    # Create the Agent
    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(
        agent=agent, 
        tools=tools, 
        verbose=True,
        handle_parsing_errors=True # Fix for "Failed to call function" / parsing errors
    )

    def format_problem_for_agent(input_dict):
        # Flatten the MathProblem object for the agent input
        prob = input_dict["structured_problem"]
        if hasattr(prob, "dict"):
            prob = prob.dict()
            
        return {
            "topic": prob.get("topic", "Math"),
            "variables": ", ".join(prob.get("variables", [])),
            "input": prob.get("problem_text", ""), # Map problem_text to 'input' for agent
            "context": input_dict.get("context", "")
        }

    # The Chain
    # We use a custom function to run the executor since it returns a dict, and we want the string 'output'
    def run_agent_executor(data):
        try:
            return agent_executor.invoke(data)["output"]
        except Exception as e:
            return f"Error executing solver: {e}"

    def safe_retrieve(x):
        try:
            input_text = x["structured_problem"]["problem_text"] if isinstance(x["structured_problem"], dict) else x["structured_problem"].problem_text
            return rag.retrieve_context(input_text)
        except Exception:
            return ""

    chain = (
        RunnablePassthrough.assign(
            context=lambda x: safe_retrieve(x)
        )
        | format_problem_for_agent
        | run_agent_executor
    )
    
    return chain

def get_evaluator_agent():
    """
    Returns a chain that critiques a given solution.
    Input: {"problem_text": str, "proposed_solution": str}
    Output: JSON with "is_correct": bool, "confidence": int, "feedback": str
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found.")
    
    # Use Llama-3.1-8b-instant for high-speed critique, avoiding limits
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=api_key,
        temperature=0.0
    )
    
    parser = JsonOutputParser()
    
    template = """You are a strict Math Evaluator. 
    You will receive a Math Problem and a Proposed Solution.
    
    Problem: {problem_text}
    Proposed Solution: {proposed_solution}
    
    Task:
    1. Verify every step of the calculation.
    2. Check the final answer.
    3. Return your assessment in JSON format.
    4. IMPORTANT: Return ONLY the JSON object. Do not include any explanation outside the JSON.
       {{
         "is_correct": boolean,
         "confidence": integer (0-100),
         "feedback": "string explaining any errors or confirming correctness"
       }}
    """
    
    prompt = ChatPromptTemplate.from_template(template)
    
    chain = (
        prompt
        | llm
        | parser
    )
    
    return chain
