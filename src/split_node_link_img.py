import re
from textnode import TextNode, TextType

##################################################################################
def split_nodes_image(old_nodes):
    """
    Parses image markdown in text nodes, replacing them with IMAGE TextNodes and preserving surrounding text as TEXT nodes.
    Raises an exception if no image markdown is found.
    """
    image_nodes = old_nodes
    img_pat = r"!\[([^\[\]]+)\]\(([^()]+)\)"
    matches = 0
    new_image_nodes = []
  
    for node in image_nodes:
        split_nodes = re.split(img_pat, node.text)
    
        for i in range(0, len(split_nodes), 3):
            if split_nodes[i] != "":
                new_image_nodes.append(TextNode(split_nodes[i], TextType.TEXT))
            
            if i + 2 < len(split_nodes):    
                matches += 1
                new_image_nodes.append(TextNode(split_nodes[i + 1], TextType.IMAGE, split_nodes[i + 2]))
    if matches == 0:
        raise Exception("Invalid image markdown")

    return new_image_nodes
##################################################################################
def split_nodes_links(old_nodes):
    """
    Parses link markdown in text nodes, replacing them with LINK TextNodes and preserving surrounding text as TEXT nodes.
    Raises an exception if no image markdown is found.
    """
    link_nodes = old_nodes
    link_pat = r"(?<!!)\[([^\[\]]+)\]\(([^()]+)\)"
    matches = 0
    new_link_nodes = []

    for node in link_nodes:
        split_nodes = re.split(link_pat, node.text)

        for i in range(0, len(split_nodes), 3):
            if split_nodes[i] != "":
                new_link_nodes.append(TextNode(split_nodes[i], TextType.TEXT))

            if i + 2 < len(split_nodes):
                matches += 1
                new_link_nodes.append(TextNode(split_nodes[i + 1], TextType.LINK, split_nodes[i + 2]))
    if matches == 0:
        raise Exception("Invalid link markdown")
    
    return new_link_nodes
##################################################################################












