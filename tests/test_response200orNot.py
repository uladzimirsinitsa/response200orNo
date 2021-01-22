
from main import get_html_from_sitemap
from main import get_links_without_tags
from main import convert_to_list_link


def test_get_html_from_sitemap():
    assert get_html_from_sitemap()[0:38] == '<?xml version="1.0" encoding="UTF-8"?>'


def test_get_links_without_tags():
    assert str(type(get_links_without_tags()))[1:-1] == str("<class 'bs4.element.ResultSet'>")[1:-1]


def test_convert_to_list_link():
    assert type(convert_to_list_link()).__name__ == 'list'
