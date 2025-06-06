from textnode import TextNode,TextType
from split_node_delimiter import split_nodes_delimiter
from split_node_link_img import split_nodes_image, split_nodes_links


##################################################################################  
def text_to_TextNodes(text):
    '''Converts a Markdown-formatted string into a list of TextNode objects,
       splitting it into images, links, and styled text (bold, italic, code).
    '''

    original_nodes = [TextNode(text, TextType.TEXT)]
    final_nodes = []

    final_nodes = split_nodes_image(original_nodes)
    final_nodes = split_nodes_links(final_nodes)
    final_nodes = split_nodes_delimiter(final_nodes, "**", TextType.BOLD)
    final_nodes = split_nodes_delimiter(final_nodes, "_", TextType.ITALIC)
    final_nodes = split_nodes_delimiter(final_nodes, "`", TextType.CODE)
    
    return final_nodes
##################################################################################
   