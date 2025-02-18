import json


def load_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def main():
    DATA_FILE = "animals_data.json"
    data = load_data(DATA_FILE)

    for fox in data:
        print(fox["name"])


if __name__ == '__main__':
    main()
