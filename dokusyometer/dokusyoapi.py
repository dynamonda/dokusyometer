#!/usr/bin/python

import math
import re
from bs4 import BeautifulSoup
import requests
import requests_cache

HEADERS = {'User-Agent': 'Mozilla/5.0'}

def get_soup(url):
    requests_cache.install_cache()
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup

def user_datas_from_id(id):
    if isinstance(id, int) == False:
        raise TypeError
    soup = get_soup('https://bookmeter.com/users/' + str(id))
    
    datas = {}
    if len(soup.find_all("header", class_="error__header")) > 0:
        datas["name"] = "NotFound"
        return datas
    
    item = soup.find("div", class_="userdata-side__name")
    datas["name"] = item.string
    profile_dl = soup.find("dl", class_="bm-details-side")
    readbooks = re.match(r'^[0-9]+', profile_dl.contents[5].text)
    datas["readbook"] = int(readbooks.group(0))
    return datas

def read_books_from_user_id(id):
    if isinstance(id, int) == False:
        raise TypeError
    base_url = 'https://bookmeter.com/users/'+str(id)+'/books/read?page='
    soup = get_soup(base_url + str(1))

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

def book_from_id(id):
    if isinstance(id, int) == False:
        raise TypeError

    soup = get_soup('https://bookmeter.com/books/' + id)
    

def main():
    pass

if __name__ == '__main__':
    main()
