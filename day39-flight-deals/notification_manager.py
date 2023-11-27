import os
from twilio.rest import Client


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
