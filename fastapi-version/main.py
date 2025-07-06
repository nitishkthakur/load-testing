from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import random
from datetime import datetime
import asyncio

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Mock weather data for now (will be replaced with real API later)
def get_mock_weather_data(city: str):
    """Mock weather data generator"""
    weather_conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Snowy"]
    return {
        "city": city,
        "temperature": random.randint(-10, 40),
        "condition": random.choice(weather_conditions),
        "humidity": random.randint(20, 90),
        "wind_speed": random.randint(5, 30),
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Main page with weather dashboard"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/weather/{city}")
async def get_weather(city: str):
    """Get weather data for a specific city"""
    weather_data = get_mock_weather_data(city)
    return weather_data

@app.get("/weather-card/{city}")
async def get_weather_card(request: Request, city: str):
    """Get weather card HTML for HTMX updates"""
    # Add delay based on city for async HTMX test
    delays = {
        "New York": 5,
        "London": 4,
        "Tokyo": 3,
        "Sydney": 2
    }
    delay = delays.get(city, 0)
    if delay > 0:
        await asyncio.sleep(delay)
    weather_data = get_mock_weather_data(city)
    return templates.TemplateResponse("weather_card.html", {
        "request": request, 
        "weather": weather_data
    })

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
