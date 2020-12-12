from bs4 import BeautifulSoup
import requests
from time import sleep
import os
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

locations = ["AR", "DZ", "AM", "AU", "AUADL", "AUBNE", "AUMEL", "AUPER", "AUSYD", "AT", "AZ", "BS", "BD", "BY", "BZ",
             "BE", "BT", "BA", "BR", "BN", "BG", "CA", "CAYMQ", "CAYTO", "CAYVR", "CL", "CN", "CO", "CR", "HR", "KH",
             "CZ", "DK", "EE", "EC", "EG", "FI", "FR", "FRPAR", "GE", "GR", "DE", "HK", "HU", "IE", "ID", "IL", "IM",
             "IN", "IS", "IT", "ITMIL", "ITROM", "JP", "KG", "KZ", "LA", "LI", "LT", "LU", "LV", "ME", "MC", "MD", "MT",
             "MX", "MY", "NL", "NO", "NP", "NZ", "PA", "PE", "PH", "PK", "PL", "PT", "RO", "RU", "SG", "KR", "ES",
             "ESBCN", "SE", "SK", "ZA", "CH", "TH", "TR", "TW", "UA", "US", "USATL", "USBOS", "USCLT", "USCHI", "USCOL",
             "USDAL", "USHOU", "USIND", "USMCI", "USLAS", "USLAX", "USMIA", "USEWR", "USNYC", "USORD", "USPHL", "USPHX",
             "USPDX", "USSFO", "USSJC", "USSEA", "USWAS", "UY", "AE", "GB", "GBCVT", "VE", "VN"]
print(headers[random.randrange(5)])


def change_locations():
    os.system("hotspotshield disconnect")
    location = locations[random.randrange(len(locations))]
    print(location)
    os.system("hotspotshield connect " + location)


if __name__ == "__main__":
    links = []
    for n in range(1, 5):
        if not (n % 2):
            print("start changing location")
            change_locations()
            print("end changing location")
        try:
            sleep(random.uniform(1, 3))
            r = requests.get('https://www.lacentrale.fr/listing?makesModelsCommercialNames=&options=&page=' + str(n) + '&regions=FR-IDF', headers=headers[random.randrange(5)])
            soup = BeautifulSoup(r.text, features='html.parser')
            anchors = soup.find_all('a', class_='searchCard__link')
            cnt = 0
            print("success on first link")
            print(n)
            try:
                for anchor in anchors:
                    print(anchor['href'])
                    cnt += 1
                    sleep(random.uniform(1, 3))
                    response = urllib.request.urlopen("https://www.lacentrale.fr" + anchor['href'])
                    webContent = response.read()
                    f = open('./data' + anchor['href'], 'wb')
                    f.write(webContent)
                    f.close
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
