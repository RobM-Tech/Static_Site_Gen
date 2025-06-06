import unittest
from markdown_to_blocks import Block_to_BlockType, BlockType

##################################################################################
class TestBlockToBlockType(unittest.TestCase):

    ##################################################################################
    def test_heading_valid(self):
        self.assertEqual(Block_to_BlockType("# Heading"), BlockType.HEADING)
        self.assertEqual(Block_to_BlockType("### Mid Heading"), BlockType.HEADING)
        self.assertEqual(Block_to_BlockType("###### Deep Heading"), BlockType.HEADING)
        self.assertEqual(Block_to_BlockType("###   Multiple spaces"), BlockType.HEADING)
    ##################################################################################
    def test_heading_invalid(self):
        with self.assertRaises(Exception):
            Block_to_BlockType("#")  # no space or text
        with self.assertRaises(Exception):
            Block_to_BlockType("####### Too many hashes")  # more than 6 hashes
        with self.assertRaises(Exception):
            Block_to_BlockType("### ")  # space but no text
        with self.assertRaises(Exception):
            Block_to_BlockType("#NoSpace")  # no space after hashes
    ##################################################################################
    def test_code_block(self):
        code = "```\nprint('hello')\n```"
        self.assertEqual(Block_to_BlockType(code), BlockType.CODE)
        incomplete = "```\nnot closed"
        self.assertEqual(Block_to_BlockType(incomplete), BlockType.PARAGRAPH)
    ##################################################################################
    def test_quote_block(self):
        self.assertEqual(Block_to_BlockType("> This is a quote"), BlockType.QUOTE)
        self.assertEqual(Block_to_BlockType("> First line\n> Second line"), BlockType.QUOTE)
    ##################################################################################
    def test_unordered_list(self):
        ul = "- item one\n- item two"
        self.assertEqual(Block_to_BlockType(ul), BlockType.UNORDERED_LIST)
        not_ul = "-item without space"
        self.assertEqual(Block_to_BlockType(not_ul), BlockType.PARAGRAPH)
    ##################################################################################
    def test_ordered_list_valid(self):
        ol = "1. First\n2. Second\n3. Third"
        self.assertEqual(Block_to_BlockType(ol), BlockType.ORDERED_LIST)
        ol_one = "1. Only one item"
        self.assertEqual(Block_to_BlockType(ol_one), BlockType.ORDERED_LIST)
    ##################################################################################
    def test_paragraph(self):
        self.assertEqual(Block_to_BlockType("Just some normal text."), BlockType.PARAGRAPH)
        self.assertEqual(Block_to_BlockType("Some **bold** and _italic_ text."), BlockType.PARAGRAPH)
    ##################################################################################
    def test_ordered_list_invalid(self):
        ol_wrong_start = "2. Starts wrong"
        with self.assertRaises(ValueError):
            Block_to_BlockType(ol_wrong_start)
        ol_skipped = "1. One\n3. Three"
        with self.assertRaises(ValueError):
            Block_to_BlockType(ol_skipped)
    ##################################################################################
    def test_invalid_heading_missing_space(self):
        malformed_heading = "###mal# formed"
        with self.assertRaises(Exception):
            Block_to_BlockType(malformed_heading)
    ##################################################################################
##################################################################################
if __name__ == '__main__':
    unittest.main()