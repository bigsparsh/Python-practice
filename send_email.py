import smtplib
import ssl

host = 'smtp.gmail.com'
port = 465

password = 'msqkwazzgbdragpm'
username = 'pythonsample4@gmail.com'


def email_sender(message, email, job):
    my_context = ssl.create_default_context()
    subject = f'New email from {email}'
    message = f'subject:{subject}\nFrom: {email}\nJob: {job}\nHey Sparsh,\n{message}'
    reciever = 'sparshsingh7586@gmail.com'
    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)
