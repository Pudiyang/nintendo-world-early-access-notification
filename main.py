import requests
from bs4 import BeautifulSoup
import smtplib
import time
from datetime import datetime
import configparser

# Read configuration from 'config.ini'
config = configparser.ConfigParser()
config.read('config.ini')

SENDER_EMAIL = config.get('config', 'SENDER_EMAIL')
RECEIVER_EMAILS = [email.strip() for email in config.get('config', 'RECEIVER_EMAILS').split(',')]
SENDER_PASSWORD = config.get('config', 'SENDER_PASSWORD')
EMAIL_SUBJECT = "Nintendo EA Alarm - EA tickets are available"

TICKET_DATE = config.get('config', 'TICKET_DATE')
TICKET_URL = "https://store.universalstudioshollywood.com/PurchaseTickets.aspx?Ref=Lite&View=CAT2"
COOKIE_STRING = config.get('config', 'COOKIE_STRING')
CHECK_INTERVAL = 60


def send_alarm():
    message = f'Subject: {EMAIL_SUBJECT}'
    with smtplib.SMTP('smtp.gmail.com', 587) as session:
        session.starttls()
        session.login(SENDER_EMAIL, SENDER_PASSWORD)
        session.sendmail(SENDER_EMAIL, RECEIVER_EMAILS, message)
        session.quit()
    print("ALARM SENT")

def get_cookies_dict(cookie_string):
    cookies_dict = {}
    for cookie in cookie_string.split(";"):
        key_value = cookie.split("=", 1)
        if len(key_value) == 2:
            key, value = [s.strip() for s in key_value]
            cookies_dict[key] = value
    return cookies_dict


def is_ticket_available(ticket_date):
        cookies_dict = get_cookies_dict(COOKIE_STRING)
        response = requests.get(TICKET_URL, cookies=cookies_dict)
        soup = BeautifulSoup(response.content, 'html.parser')
        input_elem = soup.find('input', {'id': 'EZRezCalendarDatePriceList'})
        value = input_elem['value']
        date_info = eval(value)
        return date_info[ticket_date]['Sold'] == "N"

def main():
    while True:
        if is_ticket_available(TICKET_DATE):
            send_alarm()
            break
        else:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{now}: Not available")
        time.sleep(CHECK_INTERVAL)


if __name__ == '__main__':
    main()