import smtplib
import getpass
import imghdr
import os

from email.message import EmailMessage


# Connecting to Mail Server
try:
    smtp_obj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    email = "aritralahiri17@gmail.com"
    password = os.environ.get('GMAIL_APP_PASS')
    smtp_obj.login(email, password)

except smtplib.SMTPAuthenticationError:
    print("Login Failed ... TRY Again !")
    input()

except ConnectionRefusedError:
    print("You don't have internet connection .")
    input()

else:
    # # Sending Mailixrgrjtprnktrmoh
    msg = EmailMessage()
    msg['From'] = email

    try:

        msg['To'] = input("Enter the recipient address : ")
        msg['Subject'] = input("Enter the subject line : ")
        msg.set_content(
            input("Enter Your Message body :")
        )

        isPic = input("Do you wanna send images : \n1.Y \n2.N \n").lower()

        if (isPic == 'y'):

            my_pics = ['test.jpg', 'test1.jpg', 'test2.jpg', 'test3.jpg']

            for pic in my_pics:

                with open(pic, "rb") as f:
                    file_data = f.read()
                    file_type = imghdr.what(f.name)
                    file_name = f.name

                msg.add_attachment(file_data, maintype='image',
                                   subtype=file_type, filename=file_name)

        smtp_obj.send_message(msg)
        print("Email has been sent !")
        input()

    except smtplib.SMTPRecipientsRefused:
        print("Can't find the recipient address.... Sorry !")
        input()
