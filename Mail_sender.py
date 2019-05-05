import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
connection_time = time.time()
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = #Sender email
password = "**********"
# Create a secure SSL context
context = ssl.create_default_context()
# Try to log in to server


def connect_server():
    global connection_time
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        print("Reconnected server correctly!")  # Logged correctly
        connection_time = time.time()
        return server
    except Exception as e:
        # Print any error messages to stdout
        print(e)


server = connect_server()


def send_message(to, subj, message, filename):
    if time.time() - connection_time > 60:
        global server
        server = connect_server()

    try:            # try to send mail

        msg = MIMEMultipart()  # Set variables to mail content
        msg['From'] = sender_email  # From
        msg['To'] = to  # To
        msg['Subject'] = subj  # Subject
        body = message  # Message

        try:        # try to add attachment to email
            attachment = open(filename, 'rb')
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= " + filename)
            msg.attach(part)
        except:     # If no attachment, continue without attachment
            print("No valid attachment")        # Print that message don't have any attachment

        msg.attach(MIMEText(body, 'plain'))      # Add all message content to message
        text = msg.as_string()                   # Add the body to message
        server.sendmail(sender_email, to, text)  # Send the message
        print("Mail sent correctly")
    except Exception as error:              # Any error while sending message
        print("Failed to send message")     # Print the error
        print(error)


def send_simple(to, subj, message):

    if time.time() - connection_time > 60:
        global server
        server = connect_server()
    try:  # try to send mail
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to
        msg['Subject'] = subj
        body = message

        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        server.sendmail(sender_email, to, text)
        print("Mail sent correctly")
    except Exception as error:
        print("Failed to send message")
        print(error)

