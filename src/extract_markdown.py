import re

def extract_markdown_images(text):
    text_to_ext = text
    img_pattern = r"!\[([^\[\]]+)\]\(([^()]+)\)"
    matches = []
    
    matches = re.findall(img_pattern, text_to_ext)
    if matches != []:    
        return matches
    else:
        raise Exception("Invalid image markdown")
    

def extract_markdown_links(text):
    text_to_ext = text
    link_pattern = r"(?<!!)\[([^\[\]]+)\]\(([^()]+)\)"
    matches = []

    matches = re.findall(link_pattern, text_to_ext)
    if matches != []:    
        return matches
    else:
        raise Exception("Invalid link markdown")
    

