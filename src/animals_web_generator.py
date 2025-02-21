import json
import web_generator as html

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


def generate_html_strong_info(name, value):
    return "".join([
        html.new_node("strong", children=f"{name}: "),
        value
    ])


def generate_html(animal_data):
    html_nodes = []

    for animal in animal_data:
        name = animal["name"]
        diet = animal["characteristics"]["diet"]
        location = " and ".join(animal["locations"])
        type_ = animal["characteristics"].get("type")

        name_node = html.new_node("div", children=name, css_class="card__title")
        diet_node = generate_html_strong_info("Diet", diet)
        location_node = generate_html_strong_info("Location", location)
        type_node = [generate_html_strong_info("Type", type_)] if type_ else []

        info_list = html.new_list("ul", [diet_node, location_node, *type_node])
        info_container = html.new_node("div", children=info_list, css_class="card__text")

        html_nodes.append(
            html.new_node("li", children=[name_node, info_container], css_class="cards__item"))

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
