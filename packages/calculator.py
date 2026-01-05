import math
from langchain_core.tools import tool

@tool
def calculate(expression: str) -> str:
    """
    Evaluates a mathematical expression to get a precise numerical answer.
    Useful for arithmetic, trigonometry, and complex calculations.
    Input should be a valid Python math expression string (e.g., "2 + 2", "math.sqrt(16)").
    """
    try:
        # Safe evaluation with limited scope
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        return str(eval(expression, {"__builtins__": None}, allowed_names))
    except Exception as e:
        return f"Error evaluating expression: {e}"
