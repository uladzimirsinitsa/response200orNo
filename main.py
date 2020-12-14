import requests
from bs4 import BeautifulSoup
import csv

URL = "https://casinogoodorbad.com/sitemap.xml"


def get_html_and_content():
    text_and_html_of_page = requests.get(URL).text  # Response
    return text_and_html_of_page  # возращает HTML код


def get_all_links():
    content = get_html_and_content()
    soup = BeautifulSoup(content, 'lxml')
    all_links = soup.find_all('loc')
    links = []

    for link_or_url in all_links:
        links.append(link_or_url.text)  # append list and split html tags
    return links


def response_200_or_no():
    links = get_all_links()
    for link in links:
        response = requests.get(link)
        print(link, response)


def urls_of_page_in_list_main_page():
    links = get_all_links()
    new_links = []
    for link in links:
        soup = BeautifulSoup(requests.get(link).text, 'lxml')
        soup.find_all('a')
        for url in soup.find_all('a'):
            new_links.append(url.get('href'))
    return new_links


def print_new_links():
    new_links = urls_of_page_in_list_main_page()
    print(new_links)
    print(len(new_links))


def main():
    get_all_links()
    #response_200_or_no()
    urls_of_page_in_list_main_page()
    print_new_links()


if __name__ == '__main__':
    main()
