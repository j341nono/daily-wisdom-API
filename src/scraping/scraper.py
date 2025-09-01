import requests
from bs4 import BeautifulSoup

SOURCE_URL = 'https://tomo8language.com/quotes-list-philosopher/'


def main():
    r = requests.get(SOURCE_URL)
    r.raise_for_status()
    soup = BeautifulSoup(r.content, 'lxml')

    result = []

    for heading in soup.select('.wp-block-heading'):
        philosopher = heading.get_text(strip=True)

        quotes = []
        for sibling in heading.find_all_next():
            if sibling.name == "h2" and "wp-block-heading" in sibling.get("class", []):
                break
            quote_tag = sibling.select_one('.fz-18px strong')
            if "wp-block-cocoon-blocks-balloon-ex-box-1" in sibling.get("class", []):
                quote_tag = sibling.select_one('.fz-18px strong')
                if quote_tag:
                    quotes.append(quote_tag.get_text(strip=True))
        unique_quotes = list(dict.fromkeys(quotes))
        result.append({"philosopher": philosopher, "quotes": unique_quotes})

    for item in result:
        print(item["philosopher"])
        for q in item["quotes"]:
            print("  -", q)



if __name__ == "__main__":
    main()