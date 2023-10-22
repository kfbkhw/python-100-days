import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

LAT = 36.030739
LONG = 129.373428
open_weather_api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACC_SID")
auth_token = os.environ.get("AUTH_TOKEN")
phone = os.environ.get("PHONE_NUM")
Hailey = "+821097565614"

weather_url = "https://api.openweathermap.org/data/3.0/onecall"
parameters = {
    "lat": LAT,
    "lon": LONG,
    "exclude": "current,minutely,daily",
    "appid": open_weather_api_key,
}

weather_response = requests.get(url=weather_url, params=parameters)
weather_response.raise_for_status()
hourly_weather = weather_response.json()["hourly"]
hourly_list = []
need_umbrella = False

for hour in hourly_weather[:12]:
    hourly_list.append(hour["weather"][0]["id"])

for weather in hourly_list:
    if weather < 700:
        need_umbrella = True

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

if need_umbrella:
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella ☔️",
        from_=phone,
        to=Hailey
    )
    print(message.status)
