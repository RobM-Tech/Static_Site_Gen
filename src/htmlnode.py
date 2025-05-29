

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_dic = self.props
        html = []

        if not self.props:
            return ""

        for pair in html_dic.items():
            key, value = pair
            html.append(f'{key}="{value}"')
        return " " + " ".join(html)
        
    def __repr__(self):
        return f'HTMLNode(tag={self.tag!r}, value={self.value!r}, children={self.children!r}, props={self.props!r})'
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value == None or self.value == "":
            raise ValueError("All leaf nodes must have a value.")
        if self.tag == None:
            return f"{self.value}"
        
                
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag == None or self.tag == "":
            raise ValueError("Parent node needs a tag.")
        if self.children == None:
            raise ValueError("child argument required.")
        
        
        html = f"<{self.tag}{self.props_to_html()}>"   
                
    
        for child in self.children:
            html = html + child.to_html()
        return html + f"</{self.tag}>"
