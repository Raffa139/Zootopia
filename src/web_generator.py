def new_node(node, *, children=None, css_class=None, self_closing=False):
    opening_tag = f"<{node}>"
    closing_tag = [f"</{node}>"]

    if css_class:
        opening_tag = f"{opening_tag[:-1]} class='{css_class}'>"

    if self_closing:
        opening_tag = f"{opening_tag[:-1]} />"
        closing_tag = []

    if not children or self_closing:
        return "".join([opening_tag, *closing_tag])

    return "".join([opening_tag, *children, *closing_tag])


def new_list_item(children):
    return new_node("li", children=children)


def new_list(list_node, list_items):
    item_nodes = [new_list_item(item) for item in list_items]
    return new_node(list_node, children=item_nodes)
