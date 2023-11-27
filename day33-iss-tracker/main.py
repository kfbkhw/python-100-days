import time
import requests
from datetime import datetime
import smtplib

with open("login.txt") as info:
    data = info.readlines()
    EMAIL = data[0].strip()
    PASSWORD = data[1].strip()

MY_LAT = 36.030739
MY_LONG = 129.373428

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_data = response.json()
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    lat_range = [MY_LAT - 5, MY_LAT + 5]
    lng_range = [MY_LONG - 5, MY_LONG + 5]
    if lat_range[0] <= iss_latitude <= lat_range[1] and lng_range[0] <= iss_longitude <= lng_range[1]:
        return True


def is_dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sun_data = response.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0]) - 15
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0]) + 9

    day_time = [sunrise, sunset]
    time_now = datetime.now().hour
    if day_time[0] <= time_now <= day_time[1]:
        return True


# If the ISS is close to my current position, and it is currently dark.
# Then email me to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    if is_close() and is_dark():
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.starttls()
            smtp.login(user=EMAIL, password=PASSWORD)
            smtp.sendmail(
                from_addr=EMAIL,
                to_addrs="kfbkhw@gmail.com",
                msg="Subject:ISS Over Head\n\nLook up!"
            )
