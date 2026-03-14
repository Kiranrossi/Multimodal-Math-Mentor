from langchain_community.utilities import SerpAPIWrapper
from config.config import app_config

def get_search_tool():
    """
    Returns a configured SerpAPI search wrapper.
    """
    if not app_config.SERPAPI_API_KEY:
        raise ValueError("SERPAPI_API_KEY must be set in your .env to use web search.")
    return SerpAPIWrapper(serpapi_api_key=app_config.SERPAPI_API_KEY)

def search_web(query):
    """
    Helper to search the web using SerpAPI.
    """
    tool = get_search_tool()
    try:
        return tool.run(query)
    except Exception as e:
        return f"Search failed: {e}"
