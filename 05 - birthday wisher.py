import pandas
import datetime as dt
import smtplib

data = pandas.read_csv('birthday-wisher/birthdays.csv')
birthdays = data.to_dict(orient='records')

now = dt.datetime.now()
my_email = 'philmilessmtptest@gmail.com'
password = 'byxhurnsqncsxvrp'

# looping through dictionary entries
for birthday in birthdays:
    # if conditions match, send an email
    if now.month == birthday['month'] and now.day == birthday['day'] and birthday['sent'] == 'no':
        message = f"Subject:Rođendan ti je.\n\nDanas ti je rođrendan.\nProšlo je [{now.year - birthday['year']}] " \
                  f"godina od tvog rođenja.\nSrećan rođendan. 🎉".encode('utf8')
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday['email'],
                msg=message)
            print("email sent")
        # update entry, so the birthday email goes out once a year
        birthday['sent'] = 'yes'
        data = pandas.DataFrame(birthdays)
        data.to_csv('birthday-wisher/birthdays.csv', index=False)
        print(f"csv value updated: {birthday}")
    # if birthday has passed, update 'sent' key to 'no' so that the email can be sent again, once the conditions are met
    elif now.month != birthday['month'] and birthday['sent'] == 'yes' or now.day != birthday['day'] and birthday['sent'] == 'yes':
        birthday['sent'] = 'no'
        data = pandas.DataFrame(birthdays)
        data.to_csv('birthday-wisher/birthdays.csv', index=False)
        print(f"csv value reset:{birthday}")


