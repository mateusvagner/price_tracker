"""
Price Tracker para Loja do Mecânico
https://www.lojadomecanico.com.br/
"""
import requests
from bs4 import BeautifulSoup
import  smtplib
import time

URL = 'https://www.lojadomecanico.com.br/produto/103830/21/154/maquina-de-solda-portatil-inversora-joy-162--tigdc---mma-160a-220v--balmer-30179528'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

def check_price():
       
    page = requests.get(URL, headers=headers)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    title = soup.find(class_="product-name").get_text()
    price = soup.find(id="product-price").get_text()
    converted_price = float(price[0:5]) #pega das posições 0 até a 4 (intervalo aberto)
    
    print(title.strip())
    print(converted_price)
    
    if(converted_price < 1.300):
        send_mail()
    
    
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('***@gmail.com', '***')
    
    #subject = 'O preço da Joy 162 Baixou!'
    #body = 'Acesse a Loja do Mecanico https://www.lojadomecanico.com.br/produto/103830/21/154/maquina-de-solda-portatil-inversora-joy-162--tigdc---mma-160a-220v--balmer-30179528'
    #msg = f'Subject: {subject} {body}'
    
    server.sendmail(
        '***@gmail.com',
        '***@gmail.com',
        "Acesse a Loja do Mecânico TIG JOY 162 BAIXOU"
    )
    print('O e-mail foi enviado!!!!')
    server.quit()
    
# Chamada da função
contador = 0
while(True):
    check_price()
    time.sleep(60*60)
    contador+=1
    if(contador > 24):
        break

    
    
