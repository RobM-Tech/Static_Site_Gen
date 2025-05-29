import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_eq(self):
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_Noteq(self):
        node = HTMLNode(props={
            "href": "https://www.gmail.com",
            "target": "_blank",
        })
        self.assertNotEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_dif_expe(self):
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertNotEqual(node.props_to_html(), ' href="https://www.gmail.com" target="_blank"')

    def test_empty_props(self):
        node = HTMLNode(props={})
        self.assertNotEqual(node.props_to_html(), ' href="https://www.gmail.com" target="_blank"')


#####
#Leaf Node Tests
#####

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_novalue(self):
        node = LeafNode("a", "")
        self.assertRaises(ValueError)

    def test_leaf_to_html_notag(self):
        node = LeafNode(None, "I have no tag!")
        self.assertEqual(node.to_html(), "I have no tag!")

    def test_leaf_to_html_heading(self):
        node = LeafNode("h1", "My first heading!")
        self.assertEqual(node.to_html(), "<h1>My first heading!</h1>")

    def test_leaf_to_html_noteq(self):
        node = LeafNode("body", "I should be just plain text.")
        self.assertNotEqual(node.to_html(), "I should be just plain text.")




#####
#Parent Node Tests
#####

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )
        
    

if __name__ == "__main__":
    unittest.main()


