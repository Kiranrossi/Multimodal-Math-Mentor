from langchain_community.tools import DuckDuckGoSearchRun

def get_search_tool():
    """
    Returns a configured DuckDuckGo search tool.
    """
    return DuckDuckGoSearchRun()

def search_web(query):
    """
    Helper to search the web for any concepts.
    """
    tool = get_search_tool()
    try:
        return tool.run(query)
    except Exception as e:
        return f"Search failed: {e}"
