##################### Extra Hard Starting Project ######################
import smtplib
import random, os
import datetime as dt
import pandas as pd

# 1. Update the birthdays.csv
df = pd.read_csv('birthdays.csv')
birthday_dict = df.to_dict(orient='records')
for entry in birthday_dict:
    bd_month = entry["month"]
    bd_day = entry["day"]

# 2. Check if today matches a birthday in the birthdays.csv
    now = dt.datetime.now()
    now_day = now.day
    now_month = now.month
    now_year = now.year
    if bd_month == now_month and bd_day == now_day:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        rand_letter = random.choice(os.listdir("letter_templates"))
        with open(f"letter_templates/{rand_letter}") as rand_letter:
            content = rand_letter.read()
        content = content.replace("[NAME]", entry['name'])

# 4. Send the letter generated in step 3 to that person's email address.
        my_email = entry['email']
        password = 'smth zrdd uwzp crrm'
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                msg=f"Subject:Happy Birthday {entry['name']}\n\n{content}.")



