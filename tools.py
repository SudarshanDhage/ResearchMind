from langchain.tools import tool
import requests 
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from rich import print
from dotenv import load_dotenv
load_dotenv()

tavily = TavilyClient(api_key=os.getenv("tavily-api-key"))

@tool
def web_search(query: str) -> str:
    """Search the web result on given query"""
    result = tavily.search(query=query, max_results=5)
    return str(result)
print(web_search.invoke("todays fifa ranking"))
    