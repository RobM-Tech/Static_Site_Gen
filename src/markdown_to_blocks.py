from enum import Enum


##################################################################################
def Markdown_to_Blocks(markdown):
    """
    Splits a Markdown string into separate blocks using double newlines as separators.
    Strips whitespace from each block. Raises ValueError if the input is empty.
    """

    if markdown == "":
        raise ValueError("No valid input detcted")
    
    res = markdown.split("\n\n")
    final_block = [text.strip() for text in res]    
    return final_block  
##################################################################################

class BlockType(Enum):

    ##################################################################################
    PARAGRAPH = "paragraph"           # Regular text block
    HEADING = "heading"               # Markdown heading like # Heading
    CODE = "code"                     # Fenced code block (``` or indent)
    QUOTE = "quote"                   # Blockquote starting with >
    UNORDERED_LIST = "unordered_list" # List with -, *, or +
    ORDERED_LIST = "ordered_list"     # Numbered list like 1.
    ##################################################################################

##################################################################################
def Block_to_BlockType(block):
    ##################################################################################
    if block.startswith("#"):
       
        fst_space = block.find(" ")
        split_block = block.split(" ", 1)
        char_count = 0
        ##################################################################################
        for char in split_block[0]: 
            if char == "#":
                char_count += 1
        if 1 <= char_count <= 6:
           if char_count == len(split_block[0]):
                if block[fst_space - 1] == "#":
                    if fst_space + 1 < len(block) and block[fst_space + 1:].strip() != "":
                        return BlockType.HEADING
                       
        raise Exception("Incorrect heading format found")
    ##################################################################################
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    ##################################################################################
    elif block.startswith(">"):
        return BlockType.QUOTE
    ##################################################################################
    elif block.startswith("- "):
        return BlockType.UNORDERED_LIST
    ##################################################################################
    elif block[0].isdigit() and block[1] == "." and block[2] == " ":
        lines = block.splitlines()
        count = 0
        for line in lines:
            count += 1
            if line.startswith(f"{count}. "):
                continue
            else:
                raise ValueError("Incorrect ordered list")
            
        return BlockType.ORDERED_LIST
    ##################################################################################
    else:
        return BlockType.PARAGRAPH
##################################################################################
