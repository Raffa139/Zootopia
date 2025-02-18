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


def generate_html(template, animal_data):
    html_lines = []

    for animal in animal_data:
        name = animal["name"]
        diet = animal["characteristics"]["diet"]
        locations = animal["locations"]
        location = " and ".join(locations)

        type_ = animal["characteristics"].get("type")

        html_lines.append("<li class='cards__item'>")
        html_lines.append("<div class='card__title'>")
        html_lines.append(name)
        html_lines.append("</div>")
        html_lines.append("<p class='card__text'>")

        html_lines.append("<strong>")
        html_lines.append("Diet:")
        html_lines.append("</strong>")
        html_lines.append(diet)
        html_lines.append("<br />")

        html_lines.append("<strong>")
        html_lines.append("Location:")
        html_lines.append("</strong>")
        html_lines.append(location)
        html_lines.append("<br />")

        if type_:
            html_lines.append("<strong>")
            html_lines.append("Type:")
            html_lines.append("</strong>")
            html_lines.append(type_)
            html_lines.append("<br />")

        html_lines.append("</p>")
        html_lines.append("</li>")

    output = "\n".join(html_lines)
    return template.replace(PLACEHOLDER, output)


def main():
    data = load_animal_data()
    template = load_template_html()
    content = generate_html(template, data)
    write_output_html(content)


if __name__ == '__main__':
    main()
