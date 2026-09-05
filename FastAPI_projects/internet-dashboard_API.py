import asyncio
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from fastapi import FastAPI
from OOP_book.productivity.internet_dashboard import internet_dashboard

# TODO:
# data source: internet_dashboard I made a while ago
# this script's job: maintain an API and give responses to stuff
# root gives a description of each data

app = FastAPI()
# initialize API


@app.get("/")
def read_root():
    return {"message": "Welcome to the Internet Dashboard API! Use the endpoints to fetch data.",
            "guide": "visit /docs for API documentation."}
@app.get("/crypto")
async def read_crypto_prices():
    return await internet_dashboard.fetch_crypto_prices()
@app.get("/weather")
async def read_weather(city: str = None):
    return await internet_dashboard.fetch_weather(city)
@app.get("/fact")
async def read_fact_of_the_day():
    return await internet_dashboard.fetch_fact_of_the_day()
@app.get("/word")
async def read_word_of_the_day():
    return await internet_dashboard.fetch_word_of_the_day()
@app.get("/script_count")
async def read_script_count():
    return await internet_dashboard.count_scripts_in_repo()
@app.get("/news")
async def read_news():
    return await internet_dashboard.aggregate()
@app.get("/dashboard")
async def read_dashboard(city: str = None):
    crypto_task = asyncio.create_task(internet_dashboard.fetch_crypto_prices())
    weather_task = asyncio.create_task(internet_dashboard.fetch_weather(city))
    fact_task = asyncio.create_task(internet_dashboard.fetch_fact_of_the_day())
    word_task = asyncio.create_task(internet_dashboard.fetch_word_of_the_day())
    script_count_task = asyncio.create_task(internet_dashboard.count_scripts_in_repo())
    crypto_data, weather_data, fact_data, word_data, script_count = await asyncio.gather(crypto_task, weather_task, fact_task, word_task, script_count_task)

    # Combine the results into a single response
    # ignore news since it doesn't return json

    response = {

        "crypto": crypto_data,
        "weather": weather_data,
        "fact_of_the_day": fact_data,
        "word_of_the_day": word_data,
        "script_count": script_count
    }
    return response