
import requests
import datetime
import csv
from multiprocessing import Pool
from bs4 import BeautifulSoup


URL = "https://casinogoodorbad.com/sitemap.xml"


def get_html_from_sitemap():
    """requests URL and returns HTML"""
    html_of_sitemap = requests.get(URL).text
    return html_of_sitemap


def get_links_without_tags():
    """the data is cleared of tags"""
    html_of_sitemap = get_html_from_sitemap()
    soup = BeautifulSoup(html_of_sitemap, 'lxml')
    clear_links = soup.find_all('loc')
    return clear_links


def convert_to_list_link():
    """converting an object BS to a list Python"""
    clear_links = get_links_without_tags()
    data = []
    for link in clear_links:
        data.append(link.text)
    return data


def print_and_write_csv(data):
    """outputs the requested URL and response to the console and
    writes url and response to file"""
    print(data, requests.get(data))
    with open('list_url_and_response.csv', 'a') as f:
        writer = csv.writer(f)


def main():
    """request for each page from the list"""
    start = datetime.datetime.now()
    data = convert_to_list_link()
    with Pool(16) as pool:
        pool.map(print_and_write_csv, data)
    end = datetime.datetime.now()
    total = end - start
    print(str(total))


if __name__ == '__main__':
    main()


