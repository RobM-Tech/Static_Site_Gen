from textnode import TextType, TextNode
##################################################################################
def split_nodes_delimiter(
        old_nodes: list[TextNode],
        delimiter: str,
        text_type: TextType
        ):
    """
    Splits a list of TextNode objects by a given markdown delimiter, converting
    the enclosed text to a different TextType while keeping others untouched.

    Raises:
        Exception: If the number of delimiters is not even (unmatched pair).
    """
    delimiter_dict = {
        "**": TextType.BOLD,
        "_": TextType.ITALIC,
        "`": TextType.CODE
    }
    # inital check for any delimiter
    ##################################################################################
    if delimiter not in delimiter_dict:
        raise ValueError("Unsupported delimiter")
    if delimiter_dict[delimiter] != text_type:
        raise ValueError("delimiter does not match expected text type")
    ##################################################################################
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        del_count = node.text.count(delimiter)
        if del_count % 2 != 0:
            raise Exception("Invalid markdown syntax: unmatched delimiter")

        split_nodes = node.text.split(delimiter)
    
        for i, text in enumerate(split_nodes):
            if text == "":
                continue
            
            if i % 2 == 0:
                new_nodes.append(TextNode(text, TextType.TEXT))
            else:
                new_nodes.append(TextNode(text, text_type))
    
    return new_nodes
    ##################################################################################