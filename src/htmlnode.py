



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