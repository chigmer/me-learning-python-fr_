"""
Internet Dashboard - Fetch multiple data sources concurrently using asyncio

TODO:
    - Fetch top 5 trending crypto prices to USD /
    - Fetch weather for selected address (IP fallback if no address provided) /
    - Import and integrate preexisting news aggregator /
    - Fetch fun fact of the day /
    - Fetch word of the day /
    - Get script count from repository /
    - Combine all data sources using asyncio.gather() for concurrent execution /
"""
import time
import asyncio
import aiohttp, requests
import os,sys
from bs4 import BeautifulSoup
import re
import subprocess
from pathlib import Path
from news_aggregator import aggregate
#help(news_aggregator)
#sys.exit()

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
            #await display_weather_forecast(data)
            return data
async def fetch_fact_of_the_day():
    url = "https://uselessfacts.jsph.pl/api/v2/facts/today"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data.get("text", None)

async def fetch_word_of_the_day():
    url = 'https://www.merriam-webster.com/wotd/feed/rss2'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            soup = BeautifulSoup(data, "xml")
            item = soup.find("item")
            word = item.find("title").get_text(strip=True)
            description_unparsed = item.find("description").get_text()
            
            # Get the contents of <description> as text
            # Second parse: the HTML inside <description>
            description_soup = BeautifulSoup(description_unparsed, "html.parser")
            description = description_soup.get_text()
            return word, description
async def display_word_of_the_day(word,description):
    if not word or not description:
        print("No word of the day found.")
        return
    pattern = r"(.*?)\s*//"
    match = re.search(pattern, description)
    if match:
        description = match.group(1).strip()
    print(f"\nWord of the day: {word.title()}\nDescription: {description}")

async def count_scripts_in_repo():
    """Count the number of py scripts in the current repository."""
    if Path(".temp_repo").exists():
        os.system("rm -rf .temp_repo")
    process = await asyncio.create_subprocess_exec("git", "clone", 'https://github.com/chigmer/me-learning-python-fr_', ".temp_repo")
    return_code = await process.wait()
    if return_code != 0:
        print("Failed to clone the repository.")
        return 0
    
    files = list(Path(".temp_repo").rglob("*.py"))
         
    return len(files)

async def main():
    # Fetch crypto prices and weather concurrently
    start_time = time.time()
    print("---------------\nInternet Dashboard \n\n")
    print("Fetching crypto prices. weather and fact of the day concurrently...")
    crypto_task = asyncio.create_task(fetch_crypto_prices())
    weather_task = asyncio.create_task(fetch_weather(None))  # add a city name as a parameter if you want to fetch weather for a specific city
    fact_task = asyncio.create_task(fetch_fact_of_the_day())
    word_task = asyncio.create_task(fetch_word_of_the_day())
    script_count_task = asyncio.create_task(count_scripts_in_repo())
    crypto_data, weather_data, fact_data, word_data, script_count = await asyncio.gather(crypto_task, weather_task, fact_task, word_task, script_count_task)

    # Process and display the fetched data
    print("Fetched data successfully.\n\n")


    #TODO: if a task returns None, handle it neatly instead of skipping printout

    #crypto
    print("-+-+-+-+-+-+-\n")
    if crypto_data is None:
        print("No crypto data fetched.")
    else:
        await display_crypto_prices(crypto_data)
    print("-+-+-+-+-+-+-\n")
    #weather
    if weather_data is None:
        print("No weather data fetched.")
    else:
        print("\n\n")
        await display_weather_forecast(weather_data)
    print("-+-+-+-+-+-+-\n")
    #fact of the day
    if fact_data is None:
        print("\nNo fact of the day fetched.")
    else:
        print(f"\nFact of the day: {fact_data}")
    print("-+-+-+-+-+-+-\n")
    #word of the day
    if word_data is None:
        print("\nNo word of the day fetched.")
    else:
        word, description = word_data
        await display_word_of_the_day(word, description)
    print("-+-+-+-+-+-+-\n")
    print(f"\n\nNumber of Python scripts in the repository: {script_count}")
    end_time = time.time()
    print("-+-+-+-+-+-+-\n")
    print(f"\nTotal time taken for asynchronous operations (NOT including news aggregator): {end_time - start_time:.2f} seconds")
    aggregate()
#news aggregator last since the module is synchronous and the rest of the dashboard is asynchronous. This will allow the news aggregator to run after the other tasks have completed.

if __name__ == "__main__":
     # Example usage of the fetch_word_of_the_day function
    asyncio.run(main())