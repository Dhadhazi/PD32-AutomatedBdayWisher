import pandas
import glob
import random
import datetime as dt
import smtplib

today = dt.datetime.now()
all_mails = glob.glob("letter_templates/*.txt")

my_email = ""
email_password = ""


def get_today_birthdays():
    all_birthdays = pandas.read_csv("birthdays.csv")
    return all_birthdays.loc[(all_birthdays["month"] == today.month) & (all_birthdays["day"] == today.day)]


def get_random_mail(name):
    with open(random.choice(all_mails)) as mail:
        return mail.read().replace("[NAME]", name)


def send_email(to_address, text):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=email_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_address,
                            msg=f"Subject:Happy Birthday!\n\n{text}")


today_birthdays = get_today_birthdays()

if len(today_birthdays)>0:
    for index, row in today_birthdays.iterrows():
        mail = get_random_mail(row["name"])
        send_email(to_address=row["email"], text=mail)