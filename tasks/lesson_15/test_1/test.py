import pytest
import os
from tasks.lesson_14.parser_pdf_html import LinkParserPDF, LinkParserHtml, BaseLinkParser, save_links, main

# put file in  directory lesson_15/test_1
pdf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '1.pdf')
invalid_pdf_path = '/tasks/lesson_14/test_directory/1111.pdf'
html_address = 'https://medium.com'


class TestParserPDF:
    def test_link_parser_pdf_get_links(self):
        parser = LinkParserPDF(pdf_path)
        links = parser.get_links()
        assert isinstance(links, set)
        assert len(links) > 0

    def test_save_links_pdf(self):
        save_links(LinkParserPDF, pdf_path)
        assert os.path.isfile('status_codes_200.txt')
        assert os.path.isfile('broken_links.txt')

    def test_instance_without_url(self):
        with pytest.raises(TypeError):
            LinkParserPDF()

    def test_get_links_with_invalid_path(self):
        parser = LinkParserPDF(invalid_pdf_path)
        with pytest.raises(FileNotFoundError):
            parser.get_links()

    def test_save_broken_links(self):
        expected_links = {'https://translater.google.com/', 'https://www.dyoutuber.com/',
                          'https://www.linkedintoqa.com/feed/'}
        filename = 'broken_links.txt'
        save_links(LinkParserPDF, pdf_path)
        with open(filename, 'r') as file:
            saved_links = {line.strip() for line in file.readlines()}
        assert expected_links == saved_links

    def test_main_with_pdf_input(self):
        with pytest.raises(SystemExit):
            main()


class TestParserBase:
    def test_save_valid_links(self):
        parser = BaseLinkParser()
        links = ['http://medium.com', 'http://google.com']
        parser.save_links(links, 'valid_links.txt')
        assert os.path.isfile('valid_links.txt')

    def test_save_broken_links(self):
        parser = BaseLinkParser()
        links = ['http://medium.com', 'http://google.com']
        parser.save_links(links, 'broken_links.txt')
        assert os.path.isfile('broken_links.txt')


class TestParserHTML:
    def test_get_links(self):
        parser = LinkParserHtml(html_address)
        links = parser.get_links()
        assert isinstance(links, list)
        assert len(links) > 0

    def test_save_html_links(self):
        save_links(LinkParserHtml, html_address)
        assert os.path.isfile('status_codes_200.txt')
        assert os.path.isfile('broken_links.txt')


class TestMain:
    def test_main_with_input(self):
        with pytest.raises(SystemExit):
            main()
