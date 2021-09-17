import json
import requests
from bs4 import BeautifulSoup


def get_url(origin, target, word):
    """Selects the wordreference url based on the origin language"""

    if origin == "en":
        return f"http://www.wordreference.com/{target}/translation.asp?tranword={word}"
    else:
        return f"http://www.wordreference.com/{origin}/{target}/translation.asp?spen={word}"


def format_translation(translation):
    translated_word = translation[0].split()[0]
    return translated_word


def translate(word, origin, target):
    """Translates a word from english to spanish or viceversa"""

    url = get_url(origin, target, word)
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    translations = []
    for translation in soup.find_all("td", {"class": "ToWrd"}):
        translations.append(translation.text)

        # Only the first translation is needed
        if len(translations) > 2:
            break

    return format_translation(translations[1:2])
