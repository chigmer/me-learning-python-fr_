import os
from pathlib import Path
from dotenv import load_dotenv
import sys
from datetime import date,datetime
import shelve
import time
import requests
# 1. Get the directory for this script
script_dir = Path(__file__).resolve().parent
#absolute


env_path = script_dir.parent / '.env'

# 3. Load it explicitly
load_dotenv(dotenv_path=env_path)

#print(f"Looking for .env at: {env_path}")
#print(f"Key found: {os.getenv('OWM_KEY') is not None}\n")
if os.getenv('OWM_KEY') is not None:
    API_KEY = os.getenv('OWM_KEY')
else:
    print("CRITICAL:key not found in .env")
    sys.exit(1)
def get_location():
    lat = os.getenv("MY_LAT")
    lon = os.getenv("MY_LON")
    
    if lat and lon: #added is not None for clarity
        return {"loc": (lat, lon)}                   
    try:
        data = requests.get("https://ipinfo.io/json", timeout=8)
        data.raise_for_status()
        data = data.json()      
        loc = data.get("loc", "0,0") 
        
        return {
    "loc": loc.split(",") #lat and long   
    }

    except Exception:
        return None
def check_usage(limit=699) -> tuple[bool,int]:
    """tracks how many times this script is used"""
    today = str(date.today())
    data_dir = Path(__file__).resolve().parent / ".indexdataOWM"
    
    # Create the folder if it's missing
    # parents=True handles nested folders; exist_ok=True prevents errors if it exists
    data_dir.mkdir(parents=True, exist_ok=True)
    
    db_path = data_dir / "usage_stats" # shelve adds the extension (.db, .dat, etc)
    
    # 3. Open the shelf using the full path string
    with shelve.open(str(db_path)) as db:        
        if db.get('last_run_date') != today:
            db['last_run_date'] = today
            db['daily_count'] = 0
        # 2. Check the limit
        current_count = db.get('daily_count', 0)
        
        if current_count >= limit:
            return False, current_count
        
        # 3. Increment for the current successful attempt
        db['daily_count'] += 1
        return True, db['daily_count']
def usage_limit():
    data_dir = Path(__file__).resolve().parent / ".indexdataOWM"
    data_dir.mkdir(parents=True, exist_ok=True)  # add this line
    db_path = data_dir / "call_stats"
    with shelve.open(str(db_path)) as db:
        # rest of function unchanged
        current_call = time.time()
        calls = db.get("call_list",[])
        calls = [c for c in calls if (current_call - c) < 45]
        if len(calls) >= 30: 
            return False 
        
        calls.append(current_call)
        db["call_list"] = calls 
        return True

#
   # "city": city,
#    "region": region,
#    "country": country,
  #  "loc": loc.split(",") #lat and long
    
    
       
def main():
    if usage_limit():
        try:
            location = get_location()
            if not location:
                print("unable to get location")
                sys.exit(1)
            lat = location["loc"][0]
            lon = location["loc"][1]
            usage,limit = check_usage()
            if not usage:
                print("thats enough eather checks for today.\n limit is 699 per day ")
                sys.exit()
            res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric",timeout=10)
            #print(f"Status: {res.status_code}")
            #print(f"Response: {res.text}")
            #print(f"API key: {API_KEY[:6]}")  # shows first 6 chars only, safe to print
            res.raise_for_status()                       
            
            data = res.json()
            #print(f"response:{data}")
            print("fetching successful.\n")
            # Extract safely
            

# ... (inside main after data = res.json())


            main = data.get("main", {})
            temp = main.get("temp")
            feels_like = main.get("feels_like")
            humidity = main.get("humidity")
            pressure = main.get("pressure")

            wind_speed = data.get("wind", {}).get("speed")
            wind_kmh = round(wind_speed * 3.6, 2)

# Convert Unix timestamps to readable time (H:M)
            sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%I:%M %p')
            sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%I:%M %p')

# Rain Check (Optional Key)
# returns '0' if the 'rain' key is missing from the API response
            rain_1h = data.get("rain", {}).get("1h", 0)

            print(f"--- Weather Report: {data['name']}, {data['sys']['country']} ---")
            print(f"Condition: {data['weather'][0]['main']} ({data['weather'][0]['description']})")
            print(f"Temperature: {temp}°C (Feels like {feels_like}°C)")
            print(f"Humidity: {humidity}% | Pressure: {pressure} hPa")
            print(f"Wind Speed: {wind_kmh} km/h")

            if rain_1h > 0:
                print(f"Precipitation (last 1h): {rain_1h}mm")

            print(f"Sun Cycle:  {sunrise} |  {sunset}")
            print("-" * 35)



        except Exception as e:
            print(f"bad network or API key: {e}")
            sys.exit(1)
        
    else:
        print("usage blocked: too many requests\nWait ~45 seconds")
if __name__ == "__main__":
    main()