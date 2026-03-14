import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import os
import uuid
import difflib
import ast
import re
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.tools import tool
from models.llm import get_llm
from utils.rag_utils import retrieve_context
from utils.search_utils import get_search_tool


@tool
def plot_math_function(equation_str: str) -> str:
    """
    Plots a mathematical function and returns the image path.
    The equation_str MUST be a valid Python numpy expression using 'x' and 'np.' prefixes.
    Example: 'np.sin(x)' or 'x**2 + 2*x' or 'np.log(x)'.
    DO NOT use math.sin, ONLY np.sin.
    """
    if len(equation_str) > 200:
        return "Error: Equation is too long (limit 200 characters)."
    if '__' in equation_str:
        return "Error: Unsafe equation format detected."
        
    # AST-based sandbox validation
    try:
        tree = ast.parse(equation_str, mode='eval')
        allowed_nodes = (
            ast.Expression, ast.Call, ast.Name, ast.Load,
            ast.BinOp, ast.UnaryOp, ast.operator, ast.unaryop,
            ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv, ast.Pow, ast.Mod,
            ast.UAdd, ast.USub, ast.Constant, ast.Num, ast.Attribute
        )
        for node in ast.walk(tree):
            if not isinstance(node, allowed_nodes):
                raise ValueError(f"Disallowed syntax node: {type(node).__name__}")
            if isinstance(node, ast.Name) and node.id not in ('x', 'np'):
                raise ValueError(f"Disallowed variable: {node.id}")
            if isinstance(node, ast.Attribute):
                if not isinstance(node.value, ast.Name) or node.value.id != 'np':
                    raise ValueError("Only 'np' attributes are allowed.")
    except Exception as e:
        return f"Error: Invalid or unsafe mathematical expression. ({str(e)})"

    x = np.linspace(-10, 10, 400)
    allowed_names = {k: v for k, v in np.__dict__.items() if not k.startswith('_')}
    allowed_names['x'] = x
    
    try:
        y = eval(equation_str, {"__builtins__": {}}, allowed_names)
        
        plt.figure(figsize=(6, 4))
        plt.plot(x, y)
        plt.title(f"Graph of {equation_str}")
        plt.grid(True)
        
        os.makedirs("generated_graphs", exist_ok=True)
        filepath = f"generated_graphs/plot_{uuid.uuid4().hex[:8]}.png"
        plt.savefig(filepath)
        plt.close()
        
        if "generated_images" not in st.session_state:
            st.session_state.generated_images = []
        st.session_state.generated_images.append(filepath)
        
        return f"Graph generated successfully and saved to {filepath}. Tell the user the graph has been generated."
    except Exception as e:
        return f"Error generating graph: {str(e)}"

@tool
def add_to_cheat_sheet(formula: str, description: str) -> str:
    """
    Saves an important formula and its description to the user's Cheat Sheet dashboard.
    Use this proactively whenever you explain a key mathematical formula or theorem.
    """
    if "cheat_sheet" not in st.session_state:
        st.session_state.cheat_sheet = []
    
    for item in st.session_state.cheat_sheet:
        if item["formula"] == formula:
            return "Already in cheat sheet."
            
    st.session_state.cheat_sheet.append({"formula": formula, "description": description})
    return "Successfully added to cheat sheet dashboard."

def get_chatbot_agent(embeddings, mode="Detailed"):
    llm = get_llm(temperature=0.2)
    search_tool_instance = get_search_tool()
    
    @tool
    def local_knowledge_search(query: str) -> str:
        """Useful to search the local knowledge base for specific mathematical concepts, local context, or project-specific data."""
        return retrieve_context(query, embeddings)
    
    @tool
    def web_search(query: str) -> str:
        """Useful to search the real-time web for facts, information, and general knowledge."""
        if mode != "Detailed":
            try:
                return search_tool_instance.run(query)
            except Exception as e:
                return f"Search failed: {e}"
                
        try:
            res1 = search_tool_instance.run(query)
            res2 = search_tool_instance.run(f"{query} explanation facts")
            match_ratio = difflib.SequenceMatcher(None, res1, res2).ratio()
            
            if match_ratio > 0.2:
                confidence = "High Confidence (95% - Cross-verified multiple sources)"
            else:
                confidence = "Low Confidence (Warning: Sources may conflict or data is sparse)"
                
            return f"[{confidence}]\n\nSearch Result:\n{res1}"
        except Exception as e:
            return f"Search failed: {e}"

    tools = [web_search, local_knowledge_search, plot_math_function, add_to_cheat_sheet]
    
    if mode == "Concise":
        system_prompt = """You are a highly intelligent AI assistant.
You MUST provide EXTREMELY CONCISE, SHORT, and DIRECT answers.
NEVER explain definitions or reasoning unless explicitly asked.
For math problems: SKIP the steps and ONLY output the final number, equation, or result. Limit your answer to 1-3 sentences maximum.
Use tools if necessary.
If you use a formula, consider using the add_to_cheat_sheet tool.
If the user asks for a graph, use the plot_math_function tool.
Do not use complicated formatting.
IMPORTANT RULE: When you need to call a tool, you MUST output ONLY the tool call and absolutely NO conversational text before or after it.
"""
    elif mode == "Socratic":
        system_prompt = """You are an expert Socratic Math Tutor.
If the user asks a math question, NEVER reveal the final answer immediately.
Your goal is to GUIDE the student to the answer by asking probing questions.
Example: "I see you are trying to find the roots. What formula do you think we should apply first?"
Break the problem down into tiny steps and ask the student to solve each step.

HOWEVER, if the user asks a generic question entirely unrelated to math (like "hello", "how are you", or finding a simple non-math fact), do NOT ask them probing questions or act like a math teacher. Just answer naturally and concisely.

Use tools if you need to look up facts, but still guide the user with questions for math concepts.
Use the add_to_cheat_sheet tool if discussing an important formula.
If the user asks for a graph, use the plot_math_function tool to help them visualize it.
IMPORTANT RULE: When you need to call a tool, you MUST output ONLY the tool call and absolutely NO conversational text before or after it.
"""
    else:
        system_prompt = """You are an expert Math Tutor and highly intelligent AI.
You MUST provide EXTREMELY DETAILED, IN-DEPTH, and LONG-FORM answers.
For math problems: 
1. Always start by identifying the core mathematical concept.
2. Formulate a plan and mention the formulas needed.
3. Apply the formulas and show the calculation step-by-step.
4. Explain the reasoning behind EVERY single step using clear Markdown formatting (bolding, bullet points).
5. Conclude with a final verification of why the answer makes sense.
NEVER just give the final answer. Act like a professor writing a textbook chapter.
ALWAYS use the add_to_cheat_sheet tool when introducing a new formula or theorem.
If the user asks to see a graph or visualize a formula, use the plot_math_function tool.
For general knowledge, use web search and deeply analyze the confidence of the results.
IMPORTANT RULE: When you need to call a tool, you MUST output ONLY the tool call and absolutely NO conversational text before or after it.
"""
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    
    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(
        agent=agent, 
        tools=tools, 
        verbose=True,
        handle_parsing_errors=True
    )
    
    return agent_executor
