import requests
from bs4 import BeautifulSoup
from collections import OrderedDict


SOURCE_URL: str = 'https://tomo8language.com/quotes-list-philosopher/'

HEADING_CLASS: str = "wp-block-heading"
HEADING_TAG: str = "h2"
HEADING_SELECTOR: str = f".{HEADING_CLASS}"

BALLOON_CLASS: str = "wp-block-cocoon-blocks-balloon-ex-box-1"  # 名言の吹き出しボックス
QUOTE_SELECTOR: str = ".fz-18px strong"  # 名言が入っている strong のセレクタ

REQUEST_TIMEOUT: int = 30


def scrape() -> list[dict]:
    r = requests.get(SOURCE_URL, timeout=REQUEST_TIMEOUT)
    r.raise_for_status()
    soup = BeautifulSoup(r.content, "lxml")

    results: list[dict] = []

    for heading in soup.select(HEADING_SELECTOR):
        philosopher = heading.get_text(strip=True)

        quotes: list[str] = []
        for sib in heading.find_next_siblings():
            if sib.name == HEADING_TAG and HEADING_CLASS in (sib.get("class") or []):
                break

            if BALLOON_CLASS in (sib.get("class") or []):
                for q in sib.select(QUOTE_SELECTOR):
                    text = " ".join(q.get_text(strip=True).split())  # 余分な空白を正規化
                    quotes.append(text)

        unique_quotes = list(OrderedDict.fromkeys(quotes))

        results.append({"philosopher": philosopher, "quotes": unique_quotes})

    return results


def debug_parser_1():
    r = requests.get(SOURCE_URL)
    r.raise_for_status()
    soup = BeautifulSoup(r.content, 'lxml')
    result = []
    for heading in soup.select('.wp-block-heading'):
        print(heading) # <h2 class="wp-block-heading">哲学者の名言集まとめ一覧（あいうえお順）</h2>
        import sys; sys.exit()

def debug_parser_2():
    r = requests.get(SOURCE_URL)
    r.raise_for_status()
    soup = BeautifulSoup(r.content, 'lxml')
    result = []
    for heading in soup.select('.wp-block-heading'):
        # heading : <h2 class="wp-block-heading">哲学者の名言集まとめ一覧（あいうえお順）</h2>
        philosopher = heading.get_text(strip=True)
        print(philosopher)
        import sys; sys.exit()

def debug_parser_3():
    r = requests.get(SOURCE_URL, timeout=REQUEST_TIMEOUT)
    r.raise_for_status()
    soup = BeautifulSoup(r.content, "lxml")
    results: list[dict] = []
    for heading in soup.select(HEADING_SELECTOR):
        philosopher = heading.get_text(strip=True)
        quotes: list[str] = []
        for sib in heading.find_next_siblings():
            if sib.name == HEADING_TAG and HEADING_CLASS in (sib.get("class") or []):
                break
            # print(sib.get("class"))
            if BALLOON_CLASS in (sib.get("class") or []):
                for q in sib.select(QUOTE_SELECTOR):
                    # print(q)
                    text = " ".join(q.get_text(strip=True).split())  # 余分な空白を正規化
                    quotes.append(text)
                    # print(quotes.append(text))
                    # import sys; sys.exit()
        unique_quotes = list(OrderedDict.fromkeys(quotes))
        print(unique_quotes)
        # import sys; sys.exit()


if __name__ == "__main__":
    # main()
    debug_parser_3()