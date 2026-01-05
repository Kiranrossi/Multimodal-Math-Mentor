from langchain_community.tools import DuckDuckGoSearchRun

def get_search_tool():
    """
    Returns a configured DuckDuckGo search tool.
    """
    return DuckDuckGoSearchRun()

def search_math_context(query):
    """
    Helper to search the web for math concepts.
    """
    tool = get_search_tool()
    try:
        # Append 'math definition' to context to keep it relevant
        return tool.run(f"{query} math definition application")
    except Exception as e:
        return f"Search failed: {e}"
