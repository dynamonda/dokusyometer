#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
import requests_cache

HEADERS = {'User-Agent': 'Mozilla/5.0'}

def user_datas_from_id(id):
    if isinstance(id, int) == False:
        raise TypeError

    requests_cache.install_cache()
    url = 'https://bookmeter.com/users/'
    response = requests.get(url + str(id), headers=HEADERS)
    soup = BeautifulSoup(response.text, "lxml")
    
    datas = {}
    if len(soup.find_all("header", class_="error__header")) > 0:
        datas["name"] = "NotFound"
    else:
        item = soup.find("div", class_="userdata-side__name")
        datas["name"] = item.string
    return datas

def main():
    pass

if __name__ == '__main__':
    main()
