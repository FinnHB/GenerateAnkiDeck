#-------------#
#-- IMPORTS --#
#-------------#
#Package for generating Anki decks
import genanki

#---------------------#
#-- MODEL TEMPLATES --#
#---------------------#
#Card model with basic definition and example separated with whitespaces and a black dot. Definition in Bold
GPT_MODEL = genanki.Model(
  15593830333,
  'Basic (genanki)',
  fields=[
    {
      'name': 'Front',
      'font': 'Arial',
    },
    {
      'name': 'Back-Definition',
      'font': 'Arial',
    },
    {
      'name': 'Back-Context',
      'font': 'Arial',
    },
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Front}}',
      'afmt': '{{FrontSide}}\n\n<hr id=answer><b>{{Back-Definition}}</b><br>&#x25cf<br>{{Back-Context}}',
    },
  ],
  css='.card {\n font-family: arial;\n font-size: 20px;\n text-align: center;\n color: black;\n background-color: white;\n}\n',
)