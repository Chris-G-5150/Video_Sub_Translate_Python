import json
import string

from deep_translator import GoogleTranslator

# translation part,
# 1. once text has been extracted from video send an api request for each piece to google,
# 2. parse the JSON as a string, bundle the json text all together along with the timestamp and potentially
# se a regex to recognise the numbers

# things to do
# 1. see how google behaves when being sent the numbers as well as the text,
# 2. if it is fine and doesn't obscure this should be safe to send the stringified JSON

def translate(target_language, translation_json_src, source_language = 'auto'):
    loaded_json = json.load(open(translation_json_src)) # json opened and converted to dictionary for Python to understand
    json_string = json.dumps(loaded_json, indent=4) # stringified dictionary.

    try:
        translation = GoogleTranslator(source=source_language, targetLanguage=target_language).translate(json_string)
        Output_text.delete(1.0, END)
        Output_text.insert(END, translation)
    except Exception as e:
        print(f"Translation error: {e}")