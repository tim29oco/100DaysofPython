import asyncio
import requests
from telegram import Bot

# OpenWeather and Telegram Bot API endpoints
OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY = 'your_api_key_here'
HTTP_API = 'your_bot_token_here'
CHAT_ID = your_chat_id_here


# Set location and forecast count
weather_params = {
    "lat": your_lat_here,
    "lon": your_long_here,
    "appid": API_KEY,
    "cnt": 4
}

# Request weather data
response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
data = response.json()

# Determine if it will rain
will_rain = False
for weather in range(weather_params['cnt']):
    weather_id = data['list'][weather]['weather'][0]['id']
    if weather_id < 700:
        will_rain = True
        break  # Exit loop early if rain is detected

# Set the message ba
# sed on the rain forecast
message = "Take an umbrella! 🌧️ It's going to rain." if will_rain else "No rain expected today. Enjoy your day! ☀️"

async def main():
    bot = Bot(token=HTTP_API)
    chat_id = your_chad_id_here

    # Send the message
    await bot.send_message(chat_id=chat_id, text=message)

# Run the async function
asyncio.run(main())
