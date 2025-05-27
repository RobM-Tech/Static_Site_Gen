import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_eq(self):
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
        })

        expected = ' href="https://www.google.com" target="_blank"'
        result = node.props_to_html()
        self.assertEqual(result, expected)

    def test_props_Noteq(self):
        node = HTMLNode(props={
            "href": "https://www.gmail.com",
            "target": "_blank",
        })

        expected = ' href="https://www.google.com" target="_blank"'
        result = node.props_to_html()
        self.assertNotEqual(result, expected)

    def test_props_dif_expe(self):
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
        })

        expected = ' href="https://www.gmail.com" target="_blank"'
        result = node.props_to_html()
        self.assertNotEqual(result, expected)

    def test_empty_props(self):
        node = HTMLNode(props={})
        expected = ' href="https://www.gmail.com" target="_blank"'
        result = node.props_to_html()
        self.assertNotEqual(result, expected)



if __name__ == "__main__":
    unittest.main()