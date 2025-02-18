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
    fox_names = []

    for fox in animal_data:
        fox_names.append("<li>")
        fox_names.append(fox["name"])
        fox_names.append("</li>")

    output = "\n".join(fox_names)
    return template.replace(PLACEHOLDER, output)


def main():
    data = load_animal_data()
    template = load_template_html()
    content = generate_html(template, data)
    write_output_html(content)


if __name__ == '__main__':
    main()
