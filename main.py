import os
import smtplib

EMAIL_ADDRESS = 'd20l129@psgitech.ac.in'
EMAIL_PASSWORD = 'girish202001!'

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Result'
    body = 'Success!!!'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, 'd21l605@psgitech.ac.in', msg)
