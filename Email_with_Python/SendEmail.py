from email.message import EmailMessage
import smtplib
import mimetypes
import os
import getpass


def print_message(text):
    print(f"> {text}...")


class Emailing:
    def __init__(self, mail_address):
        self.message = None
        password = getpass.getpass(">Enter Password/App Key: ")
        self.mail_server = smtplib.SMTP_SSL("smtp.gmail.com")
        print_message("Server Successfully Created")
        self.mail_server.login(mail_address, password)
        print_message("Login successful to SMTP server")

    def add_message(self):

        self.message = EmailMessage()
        self.message["From"] = input(">Enter the SENDER Email ID: ")
        self.message["To"] = input(">Enter the  RECEIVER Email ID: ")

        subject = input(">Enter Subject of the Email: ")
        self.message["Subject"] = subject
        print_message("Subject added")

        body = input(">Enter Body of the Email: ")
        self.message.set_content(body)
        print_message("Body added")

    def add_attachment(self, root_path):

        mime_type, sub_type = mimetypes.guess_type(root_path)[0].split("/", 1)
        file_name = os.path.basename(root_path)

        with open(root_path, "rb") as file_object:
            self.message.add_attachment(file_object.read(),
                                        maintype=mime_type,
                                        subtype=sub_type,
                                        filename=file_name)

        print_message("Attachment attached")

    def send(self):

        if self.message:
            self.mail_server.send_message(self.message)
            print_message("Email send successfully")
            self.message = None
        else:
            print_message("Error, Message is Empty")

