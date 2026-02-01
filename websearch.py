from mcp.server.fastmcp import FastMCP
from openai import OpenAI
import os
mcp=FastMCP("Web Search")


api_key = os.environ.get("OPENAI_API_KEY")

@mcp.tool()
def perform_websearch(query: str)-> str:
    """
    Performs a web search for a query 
    Args:
        query:the query to web search.
    """
    messages=[
        {
            "role":"system",
            "content":(
                "You are an Ai assistant that searches the web and responds to questions"
            ),
        },
        {
            "role":"user",
            "content":(
                query
            ),
        },
    ]

    client=OpenAI(api_key=api_key,base_url="https://api.openai.com/v1")

    response=client.chat.completions.create(
        model="gpt-4o-search-preview",
        messages=messages,
    )

    return response.choices[0].message.content

if __name__=="__main__":
    mcp.run()