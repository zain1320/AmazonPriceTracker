import requests
from bs4 import BeautifulSoup
import smtplib 
URL = 'https://www.amazon.ca/Echo-Studio/dp/B07NQDP34D/ref=sr_1_4?dchild=1&keywords=alexa&qid=1614922275&sr=8-4'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.345'}
page = requests.get(URL, headers=headers)

def check_price():
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:3])
    if(converted_price < 230):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price < 230):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('zainul2002ca@gmail.com','***')
    subject = 'The price has decreased!!'
    body = 'Go and check back on: https://www.amazon.ca/Echo-Studio/dp/B07NQDP34D/ref=sr_1_4?dchild=1&keywords=alexa&qid=1614922275&sr=8-4'
    msg= f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'zainul2002ca@gmail.com',
        'zainul2002@gmail.com',
        msg
    )
    print('Done')
    server.quit()

check_price()






