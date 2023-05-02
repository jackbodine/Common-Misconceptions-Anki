from bs4 import BeautifulSoup
import genanki
import re
from genanki.model import Model


url = "https://en.wikipedia.org/wiki/List_of_common_misconceptions"

def createCards():

    print("Creating cards")
    f = open('facts_modified.txt', 'r')

    deck = genanki.Deck(
        1859477349,
        'Common Misconceptions')

    # Make new model, other than CLOZE, so that i can edit it to add photos and styling. use the default cloze from github
    # as an example
    # !!!!!
    My_CLOZE_MODEL = Model(
        1674014999,
        'Cloze (Misconceptions)',
        model_type=Model.CLOZE,
        fields=[
            {
            'name': 'Text',
            'font': 'Arial',
            },
            {
            'name': 'Back Extra',
            'font': 'Arial',
            },
        ],
        templates=[
            {
            'name': 'Cloze',
            'qfmt': '{{cloze:Text}}',
            'afmt': '{{cloze:Text}}<br>\n{{Back Extra}}',
            },
        ],
        css='.card {\n font-family: arial;\n font-size: 20px;\n text-align: center;\n color: black;\n background-color: white;\n}\n\n'
            '.cloze {\n font-weight: bold;\n color: blue;\n}\n.nightMode .cloze {\n color: lightblue;\n}',
        )

    for line in f:
        line = re.sub("[\(\[].*?[\)\]]", "", line)
        line = re.sub("<", "{{c1::", line)
        line = re.sub(">", "}}", line)
        # print(line)

        note = genanki.Note(
            model=genanki.CLOZE_MODEL,
            tags=['CommonMisconceptions'],
            fields=[line])

        deck.add_note(note)
        
    genanki.Package(deck).write_to_file('CommonMisconceptions.apkg')

def readData():

    f = open('facts.txt', 'w')
    file = open('data.html')
    soup = BeautifulSoup(file, 'html.parser')
    for tag in soup.find_all('li'):
        text = tag.getText().replace("\n", "")
        fact = ' '.join(text.split())
        f.write(f"{fact}\n")
        print(fact)
        print("")
    # print(soup.body.contents[5].contents[9].contents[13].div.ul)

createCards()
print("Done")
