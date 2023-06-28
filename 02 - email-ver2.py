# philmilessmtptest@gmail.com
# philmilessmtptest@yahoo.com
# gmail SMTP: smtp.gmail.com
# yahoo SMTP: smtp.mail.yahoo.com
# hotmail SMTP: smtp.live.com

import smtplib

my_email = 'philmilessmtptest@gmail.com'
password = 'byxhurnsqncsxvrp'
recipient = 'philmilessmtptest@yahoo.com'

# we can use the with keyword to auto-close the connection
with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=recipient,
        msg='Subject:Hello\n\nThis is the body of my email.'
    )
