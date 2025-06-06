import unittest
from textnode import TextNode, TextType
from markdown_to_blocks import Markdown_to_Blocks
##################################################################################
class TestMarkdownToBlocks(unittest.TestCase):

    ##################################################################################
    def test_multiple_blocks(self):
        md = "Block one\n\nBlock two\n\nBlock three"
        result = Markdown_to_Blocks(md)
        expected = ["Block one", "Block two", "Block three"]
        self.assertEqual(result, expected)
    ##################################################################################
    def test_single_block(self):
        md = "Just one block"
        result = Markdown_to_Blocks(md)
        expected = ["Just one block"]
        self.assertEqual(result, expected)
    ##################################################################################
    def test_extra_whitespace(self):
        md = "  Line with space  \n\n  Another one  "
        result = Markdown_to_Blocks(md)
        expected = ["Line with space", "Another one"]
        self.assertEqual(result, expected)
    ##################################################################################
    def test_empty_string_raises(self):
        with self.assertRaises(ValueError):
            Markdown_to_Blocks("")
    ##################################################################################
    def test_markdown_with_bold_and_italic(self):
        input_text = "# Heading\n\nThis is **bold** text.\n\n_Italic_ and **bold** are cool."
        expected_output = [
            "# Heading",
            "This is **bold** text.",
            "_Italic_ and **bold** are cool."
        ]
        result = Markdown_to_Blocks(input_text)
        self.assertEqual(result, expected_output)
        
if __name__ == '__main__':
    unittest.main()