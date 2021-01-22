
import requests
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


def check_link_response():
    """request for each page from the list"""
    data = convert_to_list_link()
    for link in data:
        response = requests.get(link)
        print(link, response)


def main():
    check_link_response()


if __name__ == '__main__':
    main()
