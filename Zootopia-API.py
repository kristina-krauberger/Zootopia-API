import requests

NAME = 'Fox'
API_URL = 'https://api.api-ninjas.com/v1/animals?name={}'.format(NAME)
API_KEY = 'S5Nz5En+THigkRyssS/X2g==kVACdK74PDq57ZM6'


"""
Schritte:
1. API-Anfrage gemacht und Antwort erhalten (Liste von Dictionaries)
2. HTML-Template-Datei gelesen und Inhalt in eine Variable gespeichert
3. API-Antwort parsen (z.B. animals = response.json()) und HTML-Code für jedes Tier generieren)
"""

#2. HTML Template Loader
def load_html_template(file_name):
    with open(file_name, "r", encoding="utf-8") as fileobj:
        return fileobj.read()


#3. Einzelnes Tier in HTML verwandeln
def serialize_animal(animal):
    """Erzeugt ein HTML-Snippet für ein einzelnes Tier."""
    output = "<li class='cards__item'>"
    output += f"<div class='card__title'>{animal.get('name', 'Unknown')}</div>"
    output += "<p class='card__text'>"
    output += f"<strong>Diet:</strong> {animal.get('characteristics', {}).get('diet', '--')}<br/>"
    output += f"<strong>Location:</strong> {animal.get('locations', ['--'])[0]}<br/>"
    output += f"<strong>Type:</strong> {animal.get('characteristics', {}).get('type', '--')}<br/>"
    output += "</p>"
    output += "</li>"
    return output


#4. Alle Tiere in HTML verwandeln
def show_info(animals_data):
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)
    return output


#5. Ergebnis in HTML Datei speichern
def safe_to_file(text, file_name):
    """Speichert den finalen HTML-String in eine Datei."""
    with open(file_name, "w", encoding="utf-8") as fileobj:
        fileobj.write(text)


def main():
    response = requests.get(API_URL, headers={'X-Api-Key': API_KEY})

    if response.status_code == requests.codes.ok:
        animals = response.json()  # 1. "animals" enthält deine Tierdaten (Liste von Dictionaries)
        template = load_html_template("animals_template.html")  # 2. "template" enthält den kompletten HTML-Text aus deiner Datei animals_template.html.
        animal_info = show_info(animals)  # <-- nutzt deine alten Funktionen
        final_html = template.replace("__REPLACE_ANIMALS_INFO__", animal_info) # 5.
        safe_to_file(final_html, "animals.html")
        print("Website successfully generated!")
    else:
        print("Error:", response.status_code, response.text)


if __name__ == "__main__":
    main()
