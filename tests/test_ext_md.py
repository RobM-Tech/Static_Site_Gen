import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):

    ## Tests for image markdown

    def test_EMI_two_img(self):
        test_text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(test_text)
        expected = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertEqual(result, expected)

    def test_EMI_exception(self):
        test_text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif)"
        
        with self.assertRaises(Exception) as context:
            extract_markdown_images(test_text)        


    ## Tets for link markdown

    def test_EMI_two_link(self):
        test_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(test_text)
        expected = [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]
        self.assertEqual(result, expected)

    def test_EML_exception(self):
        test_text = "This is text with a link to boot dev](https://www.boot.dev)"
        
        with self.assertRaises(Exception) as context:
            extract_markdown_links(test_text) 