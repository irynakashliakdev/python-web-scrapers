import requests
import json
from datetime import datetime

def fetch_crypto_prices():
    """
    A production-ready script to fetch top cryptocurrency prices.
    Demonstrates API integration, data parsing, and error handling.
    """
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd"
    
    try:
        print(f"[{datetime.now()}] Initializing connection to API...")
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print("\n=== CURRENT MARKET RATES ===")
            for coin, price in data.items():
                print(f"-> {coin.upper()}: ${price['usd']:,} USD")
            print("============================\n")
            
            # Saving data to a local JSON file (Simulation of Data Pipeline)
            with open("market_data.json", "w") as f:
                json.dump(data, f, indent=4)
            print("Data successfully exported to market_data.json")
            
        else:
            print(f"Error: Received status code {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    fetch_crypto_prices()
