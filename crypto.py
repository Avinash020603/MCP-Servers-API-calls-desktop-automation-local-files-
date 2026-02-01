from mcp.server.fastmcp import FastMCP
import os
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOTES_FILE = os.path.join(BASE_DIR, "notes.txt")

mcp=FastMCP("Crypto")

@mcp.tool()

def get_cryptocurrency_price(crypto: str)-> str:
    """
    Gets the price of the cryptocurrency.
    Args:
        crypto: symbol of the cryptocurrency (e.g., 'bitcoin','ethereum') .
    """

    try:
        #use the CoinGecko API to fetch current price in USD
        url=f"https://api.coingecko.com/api/v3/simple/price"
        params={"ids":crypto.lower(),"vs_currencies":"usd"}
        response=requests.get(url,params=params,timeout=10)
        response.raise_for_status()
        data=response.json()
        price=data.get(crypto.lower(),{}).get("usd")
        if price is not None:
            return f"The price of {crypto} is ${price} USD."
        else:
            return f"Price for {crypto} not found."
    except Exception as e:
        return f"Error fetching price for {crypto}: {e}"

if __name__=="__main__":
    mcp.run()