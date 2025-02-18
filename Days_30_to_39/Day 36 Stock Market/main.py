import requests
import asyncio
from itertools import islice
from telegram import Bot

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Most likely will need parameters
STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
STOCK_API_KEY = 'PBRCLAMUBQ12Z0LV'
NEWS_API_KEY = 'a39fb4dcbb79441e9ebe0f5fe26d63aa'
LANGUAGE = 'en'
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'
HTTP_API = '7971886970:AAFe4xAZQGbIQJ1Vk6vN7N-iayrSFH-B2U0'

alphavantage_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "outputsize":"compact",
    "apikey":STOCK_API_KEY
}

# Maximum of 25 Requests a day without paying for it... GAY

response = requests.get(STOCK_ENDPOINT, params=alphavantage_params)
response.raise_for_status()
data = response.json()
time_series = data["Time Series (Daily)"]
yesterday_date =  list(time_series.keys())[0]
day_b4_yesterday_date = list(time_series.keys())[1]

yesterday_data = float(data["Time Series (Daily)"][yesterday_date]["4. close"])
day_b4_yesterday_data = float(data["Time Series (Daily)"][day_b4_yesterday_date]["4. close"])

percent_difference = (yesterday_data - day_b4_yesterday_data) / day_b4_yesterday_data * 100
percent_difference = round(percent_difference, 1)
if abs(percent_difference) >= 5:

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    newsapi_params = {
        "apiKey":NEWS_API_KEY,
        "q": COMPANY_NAME,
        "language":LANGUAGE,
        "from":day_b4_yesterday_date,
        "to":yesterday_date,
        "pageSize":3
    }

    response = requests.get(NEWS_ENDPOINT, params=newsapi_params)
    response.raise_for_status()
    data = response.json()

    article_one = data['articles'][0]
    article_two = data['articles'][1]
    article_three = data['articles'][2]

    article_one_title = article_one["title"]
    article_two_title = article_two["title"]
    article_three_title = article_three["title"]

    article_one_desc = article_one["description"]
    article_two_desc = article_two["description"]
    article_three_desc = article_three["description"]

    article_dictionary = {
        article_one_title:article_one_desc,
        article_two_title:article_two_desc,
        article_three_title:article_three_desc
    }

## STEP 3: Use Telegram.
# Send a seperate message with the percentage change and each article's title and description to your phone number.

    async def main():
        bot = Bot(token=HTTP_API)
        chat_id = 6363582616
        if percent_difference >= 0:
            symbol = '🔺'
        else:
            symbol = '🔻'
        for key, value in article_dictionary.items():
            message = f"TSLA:{symbol}{percent_difference}%\n{key}\n{value}"
            await bot.send_message(chat_id=chat_id, text=message)
    asyncio.run(main())

#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

