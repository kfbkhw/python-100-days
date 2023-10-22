import os
from twilio.rest import Client
import smtplib


class NotificationManager:

    def __init__(self):
        account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        self.phone = "+12315257498"
        self.client = Client(account_sid, auth_token)

    def send_msg(self, data, recipient):
        text = f"Low price alert! Only {data.price} {data.currency} to fly from {data.from_city}-{data.from_code} " \
               f"to {data.to_city}-{data.to_code}, from {data.start_date} to {data.end_date}."
        message = self.client.messages.create(
            body=text,
            from_=self.phone,
            to=recipient,
        )
        return message.status

    def send_mail(self, data, email):
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.starttls()
            smtp.login(user="haileyprogramming@gmail.com", password="hywoogonoqkvsnpr")
            smtp.sendmail(
                from_addr="haileyprogramming@gmail.com",
                to_addrs=email,
                msg=f"Subject:New Low Price Flight!\n\nLow price alert! Only {data.price} {data.currency} to fly from {data.from_city}-{data.from_code} to {data.to_city}-{data.to_code}, from {data.start_date} to {data.end_date}.",
            )
