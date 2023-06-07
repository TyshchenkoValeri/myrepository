import argparse
import logging
import os.path
import PyPDF2
import requests
from bs4 import BeautifulSoup

logging.basicConfig(filename='parser.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)


class BaseLinkParser:
    def __init__(self, url=None):
        self.url = url
        self.logging = None

    def validate_links(self, links):
        valid_links = []
        broken_links = []
        for link in links:
            try:
                response = requests.get(link)
                status = response.status_code
                if status == 200:
                    self.logging.info(f'Response from {link} == 200')
                    valid_links.append(link)
                else:
                    self.logging.info(f'Broken from {link} is {status}')
                    broken_links.append(link)
            except requests.ConnectionError as e:
                self.logging.info(f'Broken from {link} is {e}')
                broken_links.append(link)
        return valid_links, broken_links

    @staticmethod
    def save_links(links, filename):
        with open(filename, 'w') as file:
            file.writelines(link + '\n' for link in links)


class LinkParserPDF(BaseLinkParser):

    def __init__(self, url):
        super().__init__(url)
        self.logging = logging.getLogger('[PDF]')

    def get_links(self):
        pdf_links = set()
        with open(self.url, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                annotations = page["/Annots"]
                for annot in annotations:
                    hyperlink = annot.get_object()["/A"].get_object()["/URI"]
                    pdf_links.add(hyperlink)
        return pdf_links


class LinkParserHtml(BaseLinkParser):
    def __init__(self, url):
        super().__init__(url)
        self.logging = logging.getLogger('[HTML]')

    def _get_html(self):
        if self.url:
            if not self.url.startswith('http'):
                url = os.path.join('https://', self.url)
            else:
                url = self.url
            response = requests.get(url)
            if response.status_code == 200:
                self.logging.info(f'Response from {url} == 200')
                return response.text
        else:
            return None

    def get_links(self):
        html = self._get_html()
        links = []
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            for a in soup.find_all('a', href=True):
                href = a['href']
                if not href.startswith('http'):
                    href = 'https://' + self.url + href
                links.append(href)
        return links


def save_links(instance, url):
    link_parser = instance(url=url)
    links = link_parser.get_links()
    valid_links, broken_links = link_parser.validate_links(links)
    link_parser.save_links(valid_links, 'status_codes_200.txt')
    link_parser.save_links(broken_links, 'broken_links.txt')
    logging.info("Parsing complete.")
    print("Parsing complete.")
    print(f"Valid links (status code 200) saved to status_codes_200.txt")
    print(f"Broken links saved to broken_links.txt")
    print(f"Total valid links: {len(valid_links)}")
    print(f"Total broken links: {len(broken_links)}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-url', action='store_true', help='Parse HTML page')
    parser.add_argument('-pdf', action='store_true', help='Parse PDF file')
    args = parser.parse_args()
    if args.url:
        url = input("Enter the URL: ")
        save_links(LinkParserHtml, url)
    elif args.pdf:
        url = input("Enter the path to the PDF file: ")
        save_links(LinkParserPDF, url)


if __name__ == '__main__':
    logging.info("Parsing started.")
    main()
