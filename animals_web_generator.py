from data_fetcher import fetch_data


def load_html_template(file_name):
    """
    Loads the HTML template content from a file.
    :param file_name: (str): Path to the HTML template file.
    :return: str: The content of the HTML template.
    """
    with open(file_name, "r", encoding="utf-8") as fileobj:
        return fileobj.read()


def serialize_animal(animal):
    """
    Generate an HTML snippet for a single animal.
    :param animal: (dict) : Dictionary containing information about an animal.
    :return: str: HTML snippet representing the animal.
    """
    output = "<li class='cards__item'>"
    output += f"<div class='card__title'>{animal.get('name', 'Unknown')}</div>"
    output += "<p class='card__text'>"
    output += f"<strong>Diet:</strong> {animal.get('characteristics', {}).get('diet', '--')}<br/>"
    output += f"<strong>Location:</strong> {animal.get('locations', ['--'])[0]}<br/>"
    output += f"<strong>Type:</strong> {animal.get('characteristics', {}).get('type', '--')}<br/>"
    output += "</p>"
    output += "</li>"
    return output


def show_info(animals_data):
    """
    Generate HTML list items for all animals.
    :param animals_data: (list): List of dictionaries with animal information.
    :return: str: Combined HTML snippets for all animals.
    """
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)
    return output


def safe_to_file(text, file_name):
    """
    Save the final HTML string to a file.
    :param text: (str): The HTML content to save.
    :param file_name: (str): The name of the output file.
    """
    with open(file_name, "w", encoding="utf-8") as fileobj:
        fileobj.write(text)


def main():
    """
    Main function to handle user input, fetch animal data from the API, generate HTML content, and save it to a file.
    """
    animal_name = input("Type in animal name: ").strip()
    animals = fetch_data(animal_name)

    # Validate if animals were found: proceed if the list has entries, otherwise show a "not found" message
    if animals:
        if len(animals) == 0:  # if return value is an empty list
            animal_info = f"<h2>The animal \"{animal_name}\" doesn't exist.</h2>"
        else:
            animal_info = show_info(animals)
            print("Anzahl Tiere:", len(animals))
    else:  # if return value is None
        animal_info = f"<h2>The animal \"{animal_name}\" doesn't exist.</h2>"

    template = load_html_template("animals_template.html")
    final_html = template.replace("__REPLACE_ANIMALS_INFO__", animal_info) 
    safe_to_file(final_html, "animals.html")
    print("Website successfully generated!")


if __name__ == "__main__":
    main()
