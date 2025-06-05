from textnode import TextNode, TextType
from text_to_textnodes import text_to_TextNodes
import unittest

class Test_TexttoTextNodes(unittest.TestCase):
    
    def test_text_to_TN_plain_text(self):
        result = text_to_TextNodes("Just some text.")
        expected = [TextNode("Just some text.", TextType.TEXT)]
        self.assertEqual(result, expected)
    
    def test_bold_and_italic(self):
        result = text_to_TextNodes("This is **bold** and _italic_.")
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_code_inside_sentence(self):
        result = text_to_TextNodes("Here is some `code` in a sentence.")
        expected = [
            TextNode("Here is some ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" in a sentence.", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_single_link(self):
        result = text_to_TextNodes("Check this [site](https://example.com) now.")
        expected = [
            TextNode("Check this ", TextType.TEXT),
            TextNode("site", TextType.LINK, "https://example.com"),
            TextNode(" now.", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_single_image(self):
        result = text_to_TextNodes("Here is an ![image](https://img.com/pic.png).")
        expected = [
            TextNode("Here is an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://img.com/pic.png"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_multiple_formats(self):
        result = text_to_TextNodes("Visit [site](https://x.com) and _note_ `this`.")
        expected = [
            TextNode("Visit ", TextType.TEXT),
            TextNode("site", TextType.LINK, "https://x.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("note", TextType.ITALIC),
            TextNode(" ", TextType.TEXT),
            TextNode("this", TextType.CODE),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main()