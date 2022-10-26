# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
with open('email') as fp:
    # Create a text/plain message
    msg = MIMEText(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of '
msg['From'] = 'cpureporter99@gmail.com'
msg['To'] = 'cpureporter99@gmail.com'

# Send the message via our own SMTP server, but don't include the
# envelope header.
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.sendmail('cpureporter99@gmail.com', ['cpureporter99@gmail.com'], msg.as_string())
server.quit()