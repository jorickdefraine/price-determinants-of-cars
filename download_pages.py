from bs4 import BeautifulSoup
import requests
from time import sleep
import os
import urllib.request
import random
from lxml import html
import pandas as pd
from datetime import datetime
import csv
import json

headers = [{
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'},
    {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.3'},
    {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/43.4'},
    {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'},
    {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}]

locations = ["AR", "DZ", "AM", "AU", "AUADL", "AUBNE", "AUMEL", "AUPER", "AUSYD", "AT", "AZ", "BS", "BD", "BY", "BZ",
             "BE", "BT", "BA", "BR", "BN", "BG", "CA", "CAYMQ", "CAYTO", "CAYVR", "CL", "CN", "CO", "CR", "HR", "KH",
             "CZ", "DK", "EE", "EC", "EG", "FI", "FR", "FRPAR", "GE", "GR", "DE", "HK", "HU", "IE", "ID", "IL", "IM",
             "IN", "IS", "IT", "ITMIL", "ITROM", "JP", "KG", "KZ", "LA", "LI", "LT", "LU", "LV", "ME", "MC", "MD", "MT",
             "MX", "MY", "NL", "NO", "NP", "NZ", "PA", "PE", "PH", "PK", "PL", "PT", "RO", "RU", "SG", "KR", "ES",
             "ESBCN", "SE", "SK", "ZA", "CH", "TH", "TR", "TW", "UA", "US", "USATL", "USBOS", "USCLT", "USCHI", "USCOL",
             "USDAL", "USHOU", "USIND", "USMCI", "USLAS", "USLAX", "USMIA", "USEWR", "USNYC", "USORD", "USPHL", "USPHX",
             "USPDX", "USSFO", "USSJC", "USSEA", "USWAS", "UY", "AE", "GB", "GBCVT", "VE", "VN"]

def change_locations():
    os.system("hotspotshield disconnect")
    location = locations[random.randrange(len(locations))]
    print(location)
    os.system("hotspotshield connect " + location)


# Scraping using requests+Xpath with changing header for each url

def scrap_subcar_requests(url):
    req = requests.get(url, headers=headers[random.randrange(5)])
    doc = html.fromstring(req.text)
    soup = BeautifulSoup(req.text, features='html.parser')

    try:
        name = doc.xpath('/html/body/section/section[1]/div[3]/div/div/div[1]')[0].text_content().replace('\n', '')
    except:
        name = 'NAN'
    try:
        model = doc.xpath('//*[@id="generalInformation"]/h1')[0].text_content().replace(name, '')
    except:
        model = 'NAN'
    try:
        Prix = doc.xpath('/html/body/section/section[1]/div[3]/div/div/div[2]/div/span/span')[0].text_content().replace(
            '\xa0', '').replace('\n', '')
    except:
        Prix = 'NAN'
    try:
        Mise_en_circluation = doc.xpath('//*[@id="generalInformation"]/div[2]/ul[1]/li[2]/span[2]')[0].text_content()
    except:
        Mise_en_circluation = 'NAN'
    try:
        Kilométrage_compteur = doc.xpath('//*[@id="generalInformation"]/div[2]/ul[1]/li[4]/span[2]')[0].text_content()
    except:
        Kilométrage_compteur = 'NAN'
    try:
        Energie = doc.xpath('//*[@id="generalInformation"]/div[2]/ul[1]/li[5]/span[2]')[0].text_content()
    except:
        Energie = 'NAN'
    try:
        Boite_de_vitesse = doc.xpath('//*[@id="generalInformation"]/div[2]/ul[1]/li[6]/span[2]')[0].text_content()
    except:
        Boite_de_vitesse = 'NAN'
    try:
        Nombre_de_porte = doc.xpath('//*[@id="generalInformation"]/div[2]/ul[1]/li[8]/span[2]')[0].text_content()
    except:
        Nombre_de_porte = 'NAN'
    try:
        Nombre_de_place = doc.xpath('//*[@id="generalInformation"]/div[2]/ul[1]/li[9]/span[2]')[0].text_content()
    except:
        Nombre_de_place = 'NAN'
    try:
        Puissance_fiscale = doc.xpath('//*[@id="generalInformation"]/div[2]/ul[2]/li[5]/span[2]')[
            0].text_content()  # .replace('CV','')
    except:
        Puissance_fiscale = 'NAN'
    try:
        Puissance_din = doc.xpath('//*[@id="generalInformation"]/div[2]/ul[2]/li[6]/span[2]')[0].text_content()
    except:
        Puissance_din = 'NAN'
    try:
        Consommation_mixte = doc.xpath('//*[@id="generalInformation"]/div[2]/ul[2]/li[9]/span[2]')[0].text_content()
    except:
        Consommation_mixte = 'NAN'

    try:
        Emission_CO2 = doc.xpath('//*[@id="generalInformation"]/div[2]/ul[2]/li[8]/span[2]')[
            0].text_content()  # .replace('g/kmB','') if we want to delete the suffix
    except:
        Emission_CO2 = 'NAN'

    department = soup.find_all('div', class_='cbm-outlet__information--title')[0].text[-5:].replace("(", "").replace(
        ")", "")
    post_time = soup.find_all('div', class_='cbm-toolboxButtons')[0].find_all('span')[0].text
    number_photos = len(
        json.loads(soup.find_all('div', class_="cbm-mainColumn")[0].find_all('div', {"id": "cbm-carousel"})[0].text)[
            "slides"])

    result = {'nom': name, 'model': model, 'price': Prix, 'Mise_en_circluation': Mise_en_circluation,
              'Kilométrage_compteur': Kilométrage_compteur, 'Energie': Energie, 'Boite_de_vitesse': Boite_de_vitesse,
              'Nombre_de_porte': Nombre_de_porte, 'Nombre_de_place': Nombre_de_place,
              'Puissance_fiscale': Puissance_fiscale, 'Puissance_din': Puissance_din,
              'Consommation_mixte': Consommation_mixte,
              'Emission_CO2': Emission_CO2, 'URL': url,
              'DATETIME': datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
              "department": department, "post_time": post_time, "number_photos": number_photos}

    return result


if __name__ == "__main__":
    results = []
    for n in range(1, 11):
        if not (n % 5):
            print("start changing location")
            change_locations()
            sleep(4)
            print("end changing location")


        try:
            sleep(random.uniform(0, 1))
            r = requests.get('https://www.lacentrale.fr/listing?makesModelsCommercialNames=&options=&page=' + str(
                n) + '&regions=FR-IDF', headers=headers[random.randrange(5)])
            soup = BeautifulSoup(r.text, features='html.parser')
            anchors = soup.find_all('a', class_='searchCard__link')
            cnt = 0
            print("success on first link")
            print(n)
            try:
                for anchor in anchors:
                    print(anchor['href'])
                    cnt += 1
                    sleep(random.uniform(0, 1))
                    r = scrap_subcar_requests("https://www.lacentrale.fr" + anchor['href'])
                    results.append(r)
                    df = pd.DataFrame(results)
                    df.to_csv('Cars_DB.csv', mode='w')
                    print("success on second link")
                    print(cnt)


            except:
                print("anchors")
                print(anchors)
                print("failed on second link")
                print(cnt)

        except:
            print("failed on first link")
            print(n)


