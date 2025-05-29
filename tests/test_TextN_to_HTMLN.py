import unittest
from textnode import TextNode, TextType
from TextN_to_HTMLN import text_node_to_html_node

class test_Text_to_HTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_tag(self):
        node = TextNode("Bold Text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold Text")

    def test_error(self):
        node = TextNode("Text with no value.", TextType)
        self.assertRaises(Exception, lambda: text_node_to_html_node(node))




if __name__ == "__main__":
    unittest.main()