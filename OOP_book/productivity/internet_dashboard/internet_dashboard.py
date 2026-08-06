"""
Internet Dashboard - Fetch multiple data sources concurrently using asyncio

TODO:
    - Fetch top 5 trending crypto prices to USD /
    - Fetch weather for selected address (IP fallback if no address provided)
    - Import and integrate preexisting news aggregator
    - Fetch fun fact of the day
    - Fetch word of the day
    - Get script count from repository
    - Combine all data sources using asyncio.gather() for concurrent execution
"""
import asyncio
import aiohttp, requests
import os
try:
    from dotenv import load_dotenv
except ImportError:
    # Provide a no-op fallback if python-dotenv is not installed so linters
    # and runtime don't fail. This keeps behavior similar: environment
    # variables will just be read from the environment.
    print("python-dotenv not installed, skipping .env loading. Install with 'pip install python-dotenv' to enable .env support.")
    def load_dotenv(*args, **kwargs):
        return None

load_dotenv()  # Load environment variables from .env file
#api_key = os.getenv("OWP_API_KEY")  # uncomment this line if you have an OpenWeatherMap API key and want to use it
cg_api_key = os.getenv("CG_API_KEY")  # Get the CoinGecko API key from environment variables
#print(f"API Key: {api_key}")  # Print the API key to verify it's loaded correctly
async def display_crypto_prices(data):
    """Display the crypto prices as a simple bullet list instead of a table."""
    print("Trending Crypto Prices:")
    coins = data.get("coins", [])
    if not coins:
        print("No trending coins found.")
        return []
    for coin in coins:
        item = (
            f"- {coin.get('item', {}).get('name')} ({coin.get('item', {}).get('symbol')}): "
            f"Price: ${coin.get('item', {}).get('price_btc'):.8f} BTC"
        )
        print(item)
    return coins
async def fetch_crypto_prices():
    url = f"https://api.coingecko.com/api/v3/search/trending"
    headers = {
        "Accept": "application/json",
        "X-CoinGecko-Api-Key": cg_api_key
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            data = await response.json()
            #display_crypto_prices(data)
            return data
async def get_lat_lon(city=None):
    if city is None:
        url = "http://ip-api.com/json/"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                lat = data.get("lat")
        lon = data.get("lon")
        return lat, lon
    
    elif city is not None:
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=10&language=en&format=json"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                lat = data.get("results")[0].get("latitude")
                lon = data.get("results")[0].get("longitude")
        return lat, lon
    
    print("Failed to fetch IP address.")
    return None
#print(get_lat_lon('New York'))  # Example usage of the get_lat_lon function
async def display_weather_forecast(data, max_items=12):
    """Display the weather forecast as a simple bullet list instead of a table."""
    print("Weather forecast:")

    current = data.get("current", {})
    current_units = data.get("current_units", {})
    if current:
        rain_unit = current_units.get("rain", "")
        current_line = f"- Current rain: {current.get('rain')} {rain_unit}".strip()
        print(current_line)

    hourly = data.get("hourly", {})
    hourly_units = data.get("hourly_units", {})
    times = hourly.get("time", [])
    temps = hourly.get("temperature_2m", [])
    probs = hourly.get("precipitation_probability", [])

    forecast_list = []
    for i in range(min(max_items, len(times))):
        item = (
            f"- {times[i]} | "
            f"Temp: {temps[i]}{hourly_units.get('temperature_2m', '')} | "
            f"Precipitation: {probs[i]}{hourly_units.get('precipitation_probability', '')}"
        )
        forecast_list.append(item)
        print(item)

    return forecast_list


async def fetch_weather(city=None):
    lat_lon = await get_lat_lon(city)
    #print(lat_lon)
    
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat_lon[0]}&longitude={lat_lon[1]}&hourly=temperature_2m,precipitation_probability&current=rain&timezone=auto"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            await display_weather_forecast(data)
            return data


async def main():
    # Fetch crypto prices and weather concurrently
    print("---------------\nInternet Dashboard \n\n")
    print("Fetching crypto prices and weather data concurrently...")
    crypto_task = asyncio.create_task(fetch_crypto_prices())
    weather_task = asyncio.create_task(fetch_weather(None))  # add a city name as a parameter if you want to fetch weather for a specific city

    crypto_data, weather_data = await asyncio.gather(crypto_task, weather_task)

    # Process and display the fetched data
    print("Fetched data successfully.")
    await display_crypto_prices(crypto_data)
    await display_weather_forecast(weather_data)

if __name__ == "__main__":
    asyncio.run(main())  # Example usage of the fetch_weather function