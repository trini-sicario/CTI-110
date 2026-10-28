import requests

def get_fayetteville_weather():
    # 1. Define the API URL for Open-Meteo
    url = "https://api.open-meteo.com/v1/forecast"
    
    # 2. Set up the parameters (Coordinates for Fayetteville, NC & Fahrenheit units)
    params = {
        "latitude": 35.0527,
        "longitude": -78.8784,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,wind_speed_10m",
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph"
    }
    
    print("Connecting to weather server...")
    
    try:
        # 3. Send the HTTP GET request to the API
        response = requests.get(url, params=params)
        
        # Check if the request was successful (Status code 200 means success)
        response.raise_for_status()
        
        # 4. Convert the JSON server response into a Python dictionary
        data = response.json()
        
        # 5. Extract the 'current' weather block and the 'current_units' block
        current_weather = data.get("current", {})
        units = data.get("current_units", {})
        
        # 6. Display all returned data cleanly to the terminal
        print("\n========================================")
        print("  Current Weather in Fayetteville, NC   ")
        print("========================================")
        print(f"🕒 Timestamp: {current_weather.get('time')}")
        print(f"🌡️ Temperature: {current_weather.get('temperature_2m')} {units.get('temperature_2m')}")
        print(f" sensação (Feels Like): {current_weather.get('apparent_temperature')} {units.get('apparent_temperature')}")
        print(f" 💧 Humidity: {current_weather.get('relative_humidity_2m')} {units.get('relative_humidity_2m')}")
        print(f" 🌧️ Precipitation: {current_weather.get('precipitation')} {units.get('precipitation')}")
        print(f" 💨 Wind Speed: {current_weather.get('wind_speed_10m')} {units.get('wind_speed_10m')}")
        print("========================================")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while connecting to the API: {e}")

if __name__ == "__main__":
    get_fayetteville_weather()