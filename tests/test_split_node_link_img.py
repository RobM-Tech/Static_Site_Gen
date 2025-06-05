from split_node_link_img import split_nodes_image, split_nodes_links
from textnode import TextNode, TextType
import unittest



class TestLinksandImage(unittest.TestCase):
    ##################################################################################
    # Image Tests #
    def test_SI_two_img(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_SI_multiple_nodes(self):
        nodes = [
            TextNode("Before ![one](url1.png)", TextType.TEXT),
            TextNode("After ![two](url2.png) more text", TextType.TEXT),
        ]
        new_nodes = split_nodes_image(nodes)
        self.assertListEqual(
            [
                TextNode("Before ", TextType.TEXT),
                TextNode("one", TextType.IMAGE, "url1.png"),
                TextNode("After ", TextType.TEXT),
                TextNode("two", TextType.IMAGE, "url2.png"),
                TextNode(" more text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_SI_image_at_start(self):
        node = TextNode(
            "![start](https://start.png) and some text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("start", TextType.IMAGE, "https://start.png"),
                TextNode(" and some text", TextType.TEXT),
            ],
            new_nodes,
        )
    """
    def test_SI_no_image_raises(self):
        node = TextNode("Just plain text.", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_image([node])
    """
    def test_SI_only_image(self):
        node = TextNode(
            "![alt](https://i.imgur.com/example.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("alt", TextType.IMAGE, "https://i.imgur.com/example.png"),
            ],
            new_nodes,
        )
    
    def test_SI_image_at_end(self):
        node = TextNode(
            "Some text and ![end](https://end.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Some text and ", TextType.TEXT),
                TextNode("end", TextType.IMAGE, "https://end.png"),
            ],
            new_nodes,
        )

    ##################################################################################
    # Link Tests #
    def test_SL_two_links(self): 
        node = TextNode(
            "This is a [link](https://example.com) and another [second](https://second.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second", TextType.LINK, "https://second.com"),
            ],
            new_nodes,
        )

    def test_SL_only_link(self): 
        node = TextNode(
            "[just](https://only.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("just", TextType.LINK, "https://only.com"),
            ],
            new_nodes,
        )

    def test_SL_link_at_start(self): 
        node = TextNode(
            "[start](https://start.com) followed by text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("start", TextType.LINK, "https://start.com"),
                TextNode(" followed by text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_SL_link_at_end(self): 
        node = TextNode(
            "Text before [end](https://end.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("Text before ", TextType.TEXT),
                TextNode("end", TextType.LINK, "https://end.com"),
            ],
            new_nodes,
        )
    """
    def test_SL_no_links_raises(self): 
        node = TextNode(
            "There are no links here.",
            TextType.TEXT,
        )
        with self.assertRaises(Exception) as context:
            split_nodes_links([node])
        self.assertEqual(str(context.exception), "Invalid link markdown")
    """
    def test_SL_link_and_image(self):
        node = TextNode(
            "This is a [link](https://link.com) and an ![image](https://img.com/pic.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://link.com"),
                TextNode(" and an ![image](https://img.com/pic.png)", TextType.TEXT),
            ],
            new_nodes,
        )
    
if __name__ == '__main__':
    unittest.main()