import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):


### Test All eq or not eq test
    def test_all_dif(self):
        node = TextNode("Violet is Mrs. Vi", TextType.BOLD, "https://boot.dev")
        node2 = TextNode("Gabe is the Gabber", TextType.ITALIC, "https://gmail.com")
        self.assertNotEqual(node, node2)

    def test_all_eq(self): 
        node = TextNode("I'm a tester", TextType.ITALIC, "https://boot.dev")
        node2 = TextNode("I'm a tester", TextType.ITALIC, "https://boot.dev")
        self.assertEqual(node, node2) 
###

### Test Text/TextType eq/Noteq            
    def test_Text_Noteq(self): 
        node = TextNode("I am a tester", TextType.BOLD)
        node2 = TextNode("I'm a tester", TextType.BOLD)
        self.assertNotEqual(node, node2)                   

    def test_TextType_Noteq(self): 
        node = TextNode("May the force be with you", TextType.ITALIC)
        node2 = TextNode("May the force be with you", TextType.BOLD)
        self.assertNotEqual(node, node2)                  
###

                      
    ## Test texttype and url dif
    def test_url_Noteq(self): 
        node = TextNode("I'm a tester", TextType.BOLD,)
        node2 = TextNode("I'm a tester", TextType.ITALIC, "https://boot.dev")
        self.assertNotEqual(node, node2)                   

    ## Test url with same Text/TextType
    def test_url(self):
        node = TextNode("This is the way.", TextType.BOLD,)
        node2 = TextNode("This is the way.", TextType.BOLD, "https://boot.dev")
        self.assertNotEqual(node, node2)

    ## Test url w/ same text/Texttype
    def test_dif_url(self):
        node = TextNode("What can you say", TextType.BOLD, "https://boot.dev")
        node2 = TextNode("What can you say", TextType.BOLD, "https://gmail.com")
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()