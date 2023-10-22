import requests
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
headline = []
brief = []

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_api_key = "5EYBKEP47JVDLM9P"
stock_url = "https://www.alphavantage.co/query"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key,
}

stock_response = requests.get(url=stock_url, params=stock_parameters)
yesterday = stock_response.json()["Meta Data"]["3. Last Refreshed"]
before = str(datetime.strptime(yesterday, "%Y-%m-%d").date() - timedelta(days=2))
news_date = str(datetime.strptime(yesterday, "%Y-%m-%d").date() - timedelta(days=3))
yesterday_stock = float(stock_response.json()["Time Series (Daily)"][yesterday]["4. close"])
before_stock = float(stock_response.json()["Time Series (Daily)"][before]["4. close"])

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 


def get_news():
    news_api_key = "b2fa101aa17748ce9070e4355e67fdee"
    news_url = "https://newsapi.org/v2/everything"
    news_parameters = {
        "q": COMPANY_NAME,
        "searchIn": "title",
        "from": news_date,
        "sortBy": "relevancy",
        "apiKey": news_api_key,
    }

    news_response = requests.get(url=news_url, params=news_parameters)
    for n in range(3):
        news = news_response.json()["articles"][n]
        headline.append(news["title"])
        brief.append(news["description"])


# if abs((yesterday_stock-before_stock)/yesterday_stock) >= 0.05:
#     get_news()

get_news()

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

