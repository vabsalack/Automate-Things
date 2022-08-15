from SendEmail import *


def main():
    login_email = "sskvasan552@gmail.com"
    email = Emailing(login_email)
    email.add_message()
    email.send()


if __name__ == "__main__":
    main()