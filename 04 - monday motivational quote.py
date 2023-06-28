import datetime as dt
import smtplib
from random import choice

my_email = 'philmilessmtptest@gmail.com'
password = 'byxhurnsqncsxvrp'
recipient = 'mirjanatoplicanin96@yahoo.com'
quotes_list = []

now = dt.datetime.now()


if now.weekday() == 0:
    with open('quotes.txt') as data:
        quotes_list = data.read().split("\n")
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient,
            msg=f'Subject:Monday Motivational Quote\n\n{choice(quotes_list)}'
        )