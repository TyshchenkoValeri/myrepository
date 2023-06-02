import argparse
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup


class URLValidator:
    @staticmethod
    def is_valid_url(url):
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)


class HTMLParser:
    def __init__(self, url):
        self.url = url
        self.valid_links = []
        self.broken_links = []

    def get_valid_links(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a"):
            href = link.get("href")
            if href and URLValidator.is_valid_url(href):
                self.valid_links.append(urljoin(self.url, href))
            else:
                self.broken_links.append(href)

    def validate_links(self):
        with open("status_200.txt", "w") as status_file, open("broken_links.txt", "w") as broken_file:
            for link in self.valid_links:
                response = requests.get(link)
                if response.status_code == 200:
                    status_file.write(link + "\n")
                else:
                    broken_file.write(link + "\n")

    def parse_html_page(self):
        if not URLValidator.is_valid_url(self.url):
            print("Invalid URL:", self.url)
            return

        self.get_valid_links()
        self.validate_links()
        print("Status 200 links saved to status_200.txt")
        print("Broken links saved to broken_links.txt")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="URL of the HTML page")
    args = parser.parse_args()

    url = args.url
    html_parser = HTMLParser(url)
    html_parser.parse_html_page()
