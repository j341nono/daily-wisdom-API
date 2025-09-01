import requests
from bs4 import BeautifulSoup

SOURCE_URL = 'https://tomo8language.com/quotes-list-philosopher/'


def main():
    r = requests.get(SOURCE_URL)
    r.raise_for_status()

    soup = BeautifulSoup(r.content, 'lxml')
    titles_raw = soup.select('.wp-block-heading')
    quotes_raw = soup.select('.fz-18px > strong')
    for meigen in titles_raw + quotes_raw:
        print(meigen.text)


def debug_get_data():
    r = requests.get(SOURCE_URL)
    r.raise_for_status()
    soup = BeautifulSoup(r.content, 'lxml')
    print(soup.select('.wp-block-heading'))
    print("-"*40)
    print(soup.select('.fz-18px > strong'))


def debug_parser():
    r = requests.get(SOURCE_URL)
    r.raise_for_status()
    soup = BeautifulSoup(r.content, 'lxml')
    titles_raw = soup.select('.wp-block-heading')
    quotes_raw = soup.select('.fz-18px > strong')

    titles_processed = []
    for title_raw in titles_raw:
        titles_processed.append(title_raw.text)
    print(titles_processed)
    print(f"len: {len(titles_processed)}")

    quotes_processed = []
    for quote_raw in quotes_raw:
        quotes_processed.append(quote_raw.text)
    print(quotes_processed)
    print(f"len: {len(quotes_processed)}")

if __name__ == "__main__":
    debug_parser()
