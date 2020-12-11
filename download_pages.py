from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
from time import sleep
import os
from os import path
import time
import urllib.request
import random

headers = [{
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'},
    {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.3'},
    {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/43.4'},
    {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'},
    {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}]
print(headers[random.randrange(5)])

if __name__ == "__main__":
    links = []
    for n in range(20, 3902):
        try:
            sleep(random.randint(1, 3))
            r = requests.get('https://www.lacentrale.fr/listing?makesModelsCommercialNames=&options=&page=' + str(
                n) + '&regions=FR-IDF', headers=headers[random.randrange(5)])
            soup = BeautifulSoup(r.text, features='html.parser')
            #print(soup)
            anchors = soup.find_all('a', class_='searchCard__link')
            print(anchors)
            cnt = 0
            print("success on first link")
            print(n)
            for anchor in anchors:
                cnt += 1
                try:
                    links.append("https://www.lacentrale.fr" + anchor['href'])
                    response = urllib.request.urlopen("https://www.lacentrale.fr" + anchor['href'])
                    webContent = response.read()
                    f = open('./data' + anchor['href'], 'wb')
                    f.write(webContent)
                    f.close
                    print("success on second link")
                    print(cnt)
                except:
                    print("failed on second link")
                    print(cnt)

        except:
            print("failed on first link")
            print(n)