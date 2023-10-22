import smtplib
import datetime as dt
import random

with open("login.txt") as info:
    data = info.readlines()
    EMAIL = data[0].strip()
    PASSWORD = data[1].strip()

now = dt.datetime.now()
weekday = now.weekday()

with open("quotes.txt") as quotes:
    quote_list = quotes.readlines()
    today_quote = random.choice(quote_list)

if weekday:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="kfbkhw@gmail.com",
            msg=f"Subject:Today's Quote\n\n{today_quote}"
        )
