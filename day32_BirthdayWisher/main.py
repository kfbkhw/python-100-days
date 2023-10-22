import smtplib
import datetime as dt
import random
import pandas

SENDER = "Hailey"
with open("login.txt") as info:
    data = info.readlines()
    EMAIL = data[0].strip()
    PASSWORD = data[1].strip()


def send_email():
    rand_letter = random.randint(1, 3)
    with open(f"./letter_templates/letter_{rand_letter}.txt") as letter:
        template = letter.read()
        bd_letter = template.replace("[receiver]", bd_name)
        bd_letter = bd_letter.replace("[sender]", SENDER)
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.starttls()
        smtp.login(user=EMAIL, password=PASSWORD)
        smtp.sendmail(
            from_addr=EMAIL,
            to_addrs=bd_addr,
            msg=f"Subject: Happy Birthday!\n\n{bd_letter}"
        )


with open("birthdays.csv") as file:
    df = pandas.read_csv(file)
    bd_list = pandas.DataFrame.to_dict(df, orient="records")

now = dt.datetime.now()
month = now.month
day = now.day

for bd in bd_list:
    bd_month = bd["month"]
    bd_day = bd["day"]
    if month == bd_month and day == bd_day:
        bd_name = bd["name"]
        bd_addr = bd["email"]
        send_email()
