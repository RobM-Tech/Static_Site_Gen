from textnode import TextNode,TextType
from split_node_delimiter import split_nodes_delimiter
from split_node_link_img import split_nodes_image, split_nodes_links


##################################################################################  
def text_to_TextNodes(text):
    original_nodes = [TextNode(text, TextType.TEXT)]
    final_nodes = []

    original_nodes = split_nodes_image(original_nodes)
    original_nodes = split_nodes_links(original_nodes)
    original_nodes = split_nodes_delimiter(original_nodes, "**", TextType.BOLD)
    original_nodes = split_nodes_delimiter(original_nodes, "_", TextType.ITALIC)
    original_nodes = split_nodes_delimiter(original_nodes, "`", TextType.CODE)
    final_nodes.extend(original_nodes)
    
    return final_nodes
##################################################################################
   