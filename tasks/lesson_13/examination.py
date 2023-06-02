import sys
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod


class URLValidator:
    @staticmethod
    def is_valid_url(url):
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)


class LinkSaver(ABC):
    @abstractmethod
    def save_links_to_file(self, links, filename):
        pass


class FileLinkSaver(LinkSaver):
    def save_links_to_file(self, links, filename):
        with open(filename, "w") as file:
            for link in links:
                file.write(link + "\n")


class HTMLParser:
    def __init__(self, url, link_saver):
        self.url = url
        self.valid_links = []
        self.broken_links = []
        self.link_saver = link_saver

    def get_valid_links(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a"):
            href = link.get("href")
            if href and URLValidator.is_valid_url(href):
                self.valid_links.append(urljoin(self.url, href))
            else:
                self.broken_links.append(href)

    def parse_html_page(self):
        if not URLValidator.is_valid_url(self.url):
            print("Invalid URL:", self.url)
            return

        self.get_valid_links()
        self.link_saver.save_links_to_file(self.valid_links, "status_200.txt")
        self.link_saver.save_links_to_file(self.broken_links, "broken_links.txt")

        print("Status 200 links saved to status_200.txt")
        print("Broken links saved to broken_links.txt")


if __name__ == "__main__":
    url = input("Enter the URL of the HTML page: ")
    link_saver = FileLinkSaver()
    html_parser = HTMLParser(url, link_saver)
    html_parser.parse_html_page()

