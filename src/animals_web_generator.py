import json

DATA_FILE = "animals_data.json"
TEMPLATE_FILE = "animals_template.html"
OUTPUT_FILE = "animals.html"
PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"


def load_animal_data():
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def load_template_html():
    with open(TEMPLATE_FILE, "r") as file:
        return file.read()


def write_output_html(content, ):
    with open(OUTPUT_FILE, "w") as file:
        file.write(content)


def generate_html_node(node, *, children=None, css_class=None, self_closing=False):
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


def generate_html_strong_info(name, value):
    return "".join([
        generate_html_node("strong", children=f"{name}: "),
        value
    ])


def generate_html_list_item(children):
    return generate_html_node("li", children=children)


def generate_html_list(list_node, list_items):
    item_nodes = [generate_html_list_item(item) for item in list_items]
    return generate_html_node(list_node, children=item_nodes)


def generate_html(animal_data):
    html_nodes = []

    for animal in animal_data:
        name = animal["name"]
        diet = animal["characteristics"]["diet"]
        location = " and ".join(animal["locations"])
        type_ = animal["characteristics"].get("type")

        name_node = generate_html_node("div", children=name, css_class="card__title")
        diet_node = generate_html_strong_info("Diet", diet)
        location_node = generate_html_strong_info("Location", location)
        type_node = [generate_html_strong_info("Type", type_)] if type_ else []

        info_list = generate_html_list("ul", [diet_node, location_node, *type_node])
        info_container = generate_html_node("div", children=info_list, css_class="card__text")

        html_nodes.append(
            generate_html_node("li", children=[name_node, info_container], css_class="cards__item"))

    return "\n".join(html_nodes)


def merge_html_template(template, content):
    return template.replace(PLACEHOLDER, content)


def main():
    data = load_animal_data()
    template = load_template_html()
    html_content = generate_html(data)
    merged_template = merge_html_template(template, html_content)
    write_output_html(merged_template)


if __name__ == '__main__':
    main()
