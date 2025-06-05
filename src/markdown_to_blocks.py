

##################################################################################
def Markdown_to_Blocks(markdown):
    
    if markdown == "":
        raise ValueError("No valid input detcted")
    
    res = markdown.split("\n\n")
    final_block = [text.strip() for text in res]    
    return final_block  
##################################################################################