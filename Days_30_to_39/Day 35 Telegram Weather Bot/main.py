import asyncio
import requests
from telegram import Bot

# OpenWeather and Telegram Bot API endpoints
OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY = 'c704c94064589f02d0527a5b398ca050'
HTTP_API = '7971886970:AAFe4xAZQGbIQJ1Vk6vN7N-iayrSFH-B2U0'
CHAT_ID = 6363582616


# Set location and forecast count
weather_params = {
    "lat": 40.7879,
    "lon": 74.3882,
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
    chat_id = 6363582616

    # Send the message
    await bot.send_message(chat_id=chat_id, text=message)

# Run the async function
asyncio.run(main())
