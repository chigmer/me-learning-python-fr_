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
api_key = os.getenv("OWP_API_KEY")  # Get the API key from environment variables
cg_api_key = os.getenv("CG_API_KEY")  # Get the CoinGecko API key from environment variables
#print(f"API Key: {api_key}")  # Print the API key to verify it's loaded correctly
async def fetch_crypto_prices():
    url = f"https://api.coingecko.com/api/v3/search/trending"
    headers = {
        "Accept": "application/json",
        "X-CoinGecko-Api-Key": cg_api_key
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            data = await response.json()
            return data
def get_ip_address(city=None):
    if city is None:
        url = "https://api.ipify.org?format=json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("ip")
    elif city is not None:
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=10&language=en&format=json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("ip")
    else:
        print("Failed to fetch IP address.")
        return None
    
async def fetch_weather(city=None):
    
    ip = get_ip_address(city)
    lat = ip['results'][0]['latitude']
    lon = ip['results'][0]['longitude']
    url = f"https://api.openweathermap.org/data/4.0/onecall/current?lat={lat}&lon={lon}&appid={api_key}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            print(data)
asyncio.run(fetch_weather(city="New York"))
