import sys
import os
import requests
import logging
from PyPDF2 import PdfReader

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("pdf_link_validator.log")
    ]
)


class PDFLinkExtractor:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract_links(self):
        links = []

        with open(self.file_path, "rb") as file:
            pdf_reader = PdfReader(file)
            for page in pdf_reader.pages:
                if "/Annots" in page and page["/Annots"]:
                    for annotation in page["/Annots"]:
                        annotation_obj = annotation.get_object()
                        if annotation_obj["/Subtype"] == "/Link":
                            link = annotation_obj["/A"]["/URI"]
                            links.append(link)

        return links


class LinkValidator:
    def __init__(self):
        pass

    def is_valid(self, link):
        try:
            response = requests.head(link)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False


class LinkSaver:
    def __init__(self, file_path):
        self.file_path = file_path

    def save_links(self, links):
        with open(self.file_path, "w") as file:
            for link in links:
                file.write(link + '\n')


if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    if len(sys.argv) < 3 or sys.argv[1] != "--pdf":
        file_path = input("Enter the path: ")
    else:
        file_path = sys.argv[2]

    if not os.path.isfile(file_path):
        logger.error("File does not exist.")
        sys.exit(1)

    logger.info("Start checking links in a PDF file.")

    extractor = PDFLinkExtractor(file_path)
    links = extractor.extract_links()

    validator = LinkValidator()

    valid_links = [link for link in links if validator.is_valid(link)]
    broken_links = [link for link in links if not validator.is_valid(link)]

    valid_link_saver = LinkSaver("status_codes_200.txt")
    broken_link_saver = LinkSaver("broken_links.txt")

    valid_link_saver.save_links(valid_links)
    broken_link_saver.save_links(broken_links)

    for link in broken_links:
        logger.warning("Broken link: %s", link)

    logger.info("Checking complete.")

