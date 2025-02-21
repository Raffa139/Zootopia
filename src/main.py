import animals_web_generator as web_gen
from data_fetcher import get_animal_data


def main():
    animal = input("Enter a name of an animal: ")
    data = get_animal_data(animal)
    template = web_gen.load_template_html()
    html_content = web_gen.generate_html(animal, data)
    merged_template = web_gen.merge_html_template(template, html_content)
    web_gen.write_output_html(merged_template)


if __name__ == '__main__':
    main()
