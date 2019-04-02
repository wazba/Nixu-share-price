import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
smtp_server = "smtp.gmail.com"
port = 587  # For starttls

sender_email = #SENDER EMAIL HERE
email_send = #RECIPIENTS EMAIL HERE


password = "*********"
# Create a secure SSL context
context = ssl.create_default_context()
# Try to log in to server
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()  # Can be omitted
    server.starttls(context=context)  # Secure the connection
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    print("Logged to server correctly!")  # Logged correctly
except Exception as e:
    # Print any error messages to stdout
    print(e)


def send_message(to, subj, message, filename):
    msg = MIMEMultipart()
    msg['From'] = to
    msg['To'] = email_send
    msg['Subject'] = subj
    body = message
    try:  # try to send mail
        try:  # try to add attachment to email
            attachment = open(filename, 'rb')
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= " + filename)
            msg.attach(part)
        except:
            print("No valid attachment")

        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        server.sendmail(sender_email, email_send, text)

    except Exception as error:
        print("Failed to send message")
        print(error)


def send_spam_message(to, subj, message, count, change_subject):

    try:  # try to send mail
        msg = MIMEMultipart()
        msg['From'] = to
        msg['To'] = email_send
        msg['Subject'] = subj
        body = message
        spam_subj = subj

        for i in range(0, count):
            if change_subject is True:
                subj = spam_subj + str(i)
            msg.attach(MIMEText(body, 'plain'))
            text = msg.as_string()
            server.sendmail(sender_email, email_send, text)

    except Exception as error:
        print("Failed to send message")
        print(error)
