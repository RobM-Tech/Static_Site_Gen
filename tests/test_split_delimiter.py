from split_node_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType
import unittest

class TestSplitDelimiter(unittest.TestCase):

    def test_SND_base(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(
            result,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        )

    def test_SND_start_del(self):
        node = TextNode("`code block` text after code block", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(
            result,
            [
                TextNode("code block", TextType.CODE),
                TextNode(" text after code block", TextType.TEXT)
            ]
        )

    def test_SND_end_del(self):
        # Ends with a valid code block at the end
        node = TextNode("Text before `code block`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(
            result,
            [
                TextNode("Text before ", TextType.TEXT),
                TextNode("code block", TextType.CODE)
            ]
        )

    def test_SND_multiple_del_pairs(self):
        # Two distinct code blocks in one string
        node = TextNode("Here is `code1` and `code2` blocks", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(
            result,
            [
                TextNode("Here is ", TextType.TEXT),
                TextNode("code1", TextType.CODE),
                TextNode(" and ", TextType.TEXT),
                TextNode("code2", TextType.CODE),
                TextNode(" blocks", TextType.TEXT)
            ]
        )

    def test_SND_raises_on_unmatched_delimiter(self):
        # Odd number of backticks: 1 delimiter -> invalid markdown
        node = TextNode("Here is a `broken code block", TextType.TEXT)

        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_unsupported_delimiter_raises(self):
        node = TextNode("Some text", TextType.TEXT)

        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node], "@@@", TextType.CODE)  # '@@@' not in DELIMITER_TYPE_MAP
 
    def test_mismatched_delimiter_and_texttype_raises(self):
        node = TextNode("Some `code` text", TextType.TEXT)

        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node], "`", TextType.BOLD)  # delimiter '`' expects TextType.CODE
 
if __name__ == '__main__':
    unittest.main()