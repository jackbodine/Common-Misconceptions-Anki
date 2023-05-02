import re
import genanki
from bs4 import BeautifulSoup
from genanki.model import Model

# url = "https://en.wikipedia.org/wiki/List_of_common_misconceptions"


def createCards():

    print("Creating cards")
    f = open('data.txt', 'r')

    deck = genanki.Deck(
        1859477349,
        'Common Misconceptions')

    for line in f:
        line = re.sub("[\(\[].*?[\)\]]", "", line)
        line = re.sub("<", "{{c1::", line)
        line = re.sub(">", "}}", line)

        note = genanki.Note(
            model=genanki.CLOZE_MODEL,
            tags=['CommonMisconceptions'],
            fields=[line])

        deck.add_note(note)

    genanki.Package(deck).write_to_file('CommonMisconceptions.apkg')


def readData():

    f = open('data_raw.txt', 'w')
    file = open('wiki.html')
    soup = BeautifulSoup(file, 'html.parser')

    for tag in soup.find_all('li'):
        text = tag.getText().replace("\n", "")
        fact = ' '.join(text.split())
        f.write(f"{fact}\n")


if __name__ == '__main__':
    readData()
    createCards()
    print("Done")
