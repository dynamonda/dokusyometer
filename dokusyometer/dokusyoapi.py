#!/usr/bin/python

import math
import re
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

def read_books_from_user_id(id):
    if isinstance(id, int) == False:
        raise TypeError

    requests_cache.install_cache()
    base_url = 'https://bookmeter.com/users/'+str(id)+'/books/read?page='
    response = requests.get(base_url + str(1), headers=HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    books_num = int(soup.find('div', class_='content__count').string)
    page_num = math.ceil(books_num / 20.0)

    books = list()
    for i in range(1, page_num+1):
        response = requests.get(base_url + str(i), headers=HEADERS)
        soup = BeautifulSoup(response.text, 'lxml')
        book_groups = soup.find_all('ul', class_='book-list__group')
        for book_group in book_groups:
            for book in book_group.children:
                bookdic = {}
                title = book.find('div', class_='detail__title')
                bookdic['title'] = title.a.string
                bookdic['id'] = re.search(r'([0-9]+)', title.a['href']).group(0)
                registed_date = book.find('div', class_="detail__date").string
                bookdic['registed_date'] = registed_date
                href_review = book.find('a', class_="icon__review")
                if href_review is not None:
                    href_review_id = href_review['href']
                    bookdic['review_id'] = re.search(r'([0-9]+)', href_review_id)
                books.append(bookdic)
    return books

def main():
    pass

if __name__ == '__main__':
    main()
