# importing req files
import requests
from bs4 import BeautifulSoup
import smtplib

# url for the product we want to moniter
URL = "https://www.amazon.ca/Powerbeats-Pro-Totally-Wireless-Earphones/dp/B07R5QD598/ref=sr_1_9?crid=1F0MM0WVTQMZD" \
      "&keywords=beats+wireless&qid=1562347435&s=gateway&sprefix=beats+%2Caps%2C219&sr=8-9 "
# use your user agent
# user agent can be found on google by searching 'my user agent'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/75.0.3770.100 Safari/537.36"}
# the price you want the product to be at
desired_price = 0

def send_email():
    # smtp server for your email address
    # here is an example of gmail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    your_email = 'abc@gmail.com'
    your_password = '000000'
    receiver_email = 'xyc@gmail.vom'

    server.login(your_email, your_password)
    subject = "Discount on the desired product"

    msg = f"Subject : {subject}\n\n{'check amazon link ' + URL}"
    # server.sendmail(your_email, receiver_email, msg)
    print('email has been sent')
    server.quit()


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'lxml')

    title_div = BeautifulSoup(page.content, 'html.parser')

    title = title_div.find(id='productTitle').get_text().strip()

    price = soup.find('span', {'class': 'a-color-price'})

    # changing the price to an float from str and stripping everything else
    price_float = 0.0
    for t in price.text.split():
        try:
            price_float += float(t)
        except ValueError:
            pass

    if price_float < desired_price:
        send_email()


check_price()
