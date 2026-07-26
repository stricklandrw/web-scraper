import unittest
from crawl import get_first_paragraph_from_html, get_heading_from_html


class TestCrawl(unittest.TestCase):
    def test_get_heading_from_html_basic(self):
        input_body = "<html><body><h1>Test Title</h1></body></html>"
        actual = get_heading_from_html(input_body)
        expected = "Test Title"
        self.assertEqual(actual, expected)

    def test_get_heading2_from_html_basic(self):
        input_body = "<html><body><h2>Test Title</h2></body></html>"
        actual = get_heading_from_html(input_body)
        expected = "Test Title"
        self.assertEqual(actual, expected)

    def test_get_no_heading_from_html_basic(self):
        input_body = "<html><body><p>Test Title</p></body></html>"
        actual = get_heading_from_html(input_body)
        expected = ""
        self.assertEqual(actual, expected)

    # def test_get_heading_after_h2_from_html_basic(self):
    #     input_body = """<html><body>
    #         <h2>Wrong Title</h2>
    #         <h1>Test Title</h1>
    #     </body></html>"""
    #     actual = get_heading_from_html(input_body)
    #     expected = "Test Title"
    #     self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html_main_priority(self):
        input_body = """<html><body>
            <p>Outside paragraph.</p>
            <main>
                <p>Main paragraph.</p>
            </main>
        </body></html>"""
        actual = get_first_paragraph_from_html(input_body)
        expected = "Main paragraph."
        self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html_no_main(self):
        input_body = """<html><body>
            <p>Main paragraph.</p>
            <p>Outside paragraph.</p>
        </body></html>"""
        actual = get_first_paragraph_from_html(input_body)
        expected = "Main paragraph."
        self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html_no_paragraph(self):
        input_body = "<html><body><h1>Test Title</h1></body></html>"
        actual = get_first_paragraph_from_html(input_body)
        expected = ""
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()