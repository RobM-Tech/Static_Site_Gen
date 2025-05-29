from textnode import TextNode, TextType
from htmlnode import LeafNode

def text_node_to_html_node(text_node):   
    if text_node.text_type == TextType.TEXT:
        text = LeafNode(tag=None, value=text_node.text)
        return text
    
    elif text_node.text_type == TextType.BOLD:
        bold = LeafNode(tag="b", value=text_node.text)
        return bold
    
    elif text_node.text_type == TextType.ITALIC:
        italic = LeafNode(tag="i", value=text_node.text)
        return italic
    
    elif text_node.text_type == TextType.CODE:
        code = LeafNode(tag="code", value=text_node.text)
        return code
    
    elif text_node.text_type == TextType.LINK:
        link = LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        return link
    
    elif text_node.text_type == TextType.IMAGE:
        image = LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
        return image
    
    else:
        raise Exception("Not a text type.")