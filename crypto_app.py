import requests

def get_crypto_prices():
    # 1. Define the CoinGecko Simple Price API URL
    url = "https://api.coingecko.com/api/v3/simple/price"
    
    # 2. Set up the parameters (Which coins we want, currency, and extra metrics)
    params = {
        "ids": "bitcoin,ethereum,solana,cardano",
        "vs_currencies": "usd",
        "include_market_cap": "true",
        "include_24hr_change": "true",
        "include_last_updated_at": "true"
    }
    
    print("Connecting to CoinGecko server...")
    
    try:
        # 3. Send the HTTP GET request to the API
        response = requests.get(url, params=params)
        
        # Check if the request was successful (200 = Success)
        response.raise_for_status()
        
        # 4. Convert the JSON response into a Python dictionary
        data = response.json()
        
        # 5. Display all returned data cleanly to the terminal
        print("\n========================================")
        print("    Live Cryptocurrency Market Data     ")
        print("========================================")
        
        # Loop through each coin returned in the dictionary
        for coin_id, details in data.items():
            print(f"\n🪙 Coin: {coin_id.upper()}")
            print(f"   💰 Price: ${details.get('usd'):,.2f} USD")
            print(f"   📊 Market Cap: ${details.get('usd_market_cap'):,.0f}")
            print(f"   📈 24h Change: {details.get('usd_24h_change'):.2f}%")
            
        print("\n========================================")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while connecting to the API: {e}")

if __name__ == "__main__":
    get_crypto_prices()