from tavily import TavilyClient
from config.config import app_config

class TavilyWrapper:
    def __init__(self, api_key):
        self.client = TavilyClient(api_key=api_key)
        
    def run(self, query):
        try:
            response = self.client.search(query, search_depth="basic")
            results = response.get("results", [])
            if not results:
                return "No results found."
            return "\n".join([f"- {r['content']}" for r in results])
        except Exception as e:
            return f"Search failed: {e}"

def get_search_tool():
    """
    Returns a configured Tavily search wrapper.
    """
    if not app_config.TAVILY_API_KEY:
        raise ValueError("TAVILY_API_KEY must be set in your .env to use web search.")
    return TavilyWrapper(api_key=app_config.TAVILY_API_KEY)

def search_web(query):
    """
    Helper to search the web using Tavily.
    """
    tool = get_search_tool()
    return tool.run(query)
