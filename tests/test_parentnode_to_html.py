import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
    def test_parent_tag_none(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        self.assertRaises(ValueError, lambda: parent_node.to_html())
    
    def test_parent_tag_estr(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("", [])
        self.assertRaises(ValueError, lambda: parent_node.to_html())
    
    def test_parent_no_child(self):
        parent_node = ParentNode("div", None)
        self.assertRaises(ValueError, lambda: parent_node.to_html())
    
    def test_parent_empty_child(self):
        child_node = LeafNode("span", "")
        parent_node = ParentNode("div", [child_node])
        self.assertRaises(ValueError, lambda: parent_node.to_html())
    
    def test_multiple_children(self):
        child1_node = LeafNode("span", "one")
        child2_node = LeafNode("b", "two")
        parent_node = ParentNode("div", [child1_node, child2_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>one</span><b>two</b></div>",
    )

    def test_parent_with_props(self):
        child_node = LeafNode("b", "child")
        parent_node = ParentNode("div", [child_node], props={"href": "prop test"})
        self.assertEqual(
            parent_node.to_html(),
            '<div href="prop test"><b>child</b></div>'
        )

    def test_child_with_props(self):
        child_node = LeafNode("span", "child", props={"href": "child prop test"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span href="child prop test">child</span></div>'
        )

    def test_grandchild_with_props(self):
        grandchild_node = LeafNode("b", "grandchild", props={"href": "grandchild prop test"})
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span><b href="grandchild prop test">grandchild</b></span></div>'
        )

if __name__ == "__main__":
    unittest.main()