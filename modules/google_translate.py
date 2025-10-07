# import json
# from deep_translator import GoogleTranslator

# # TODO - get the audio text to speeched
# #


# def translate(target_language, translation_json_src, source_language="auto"):
#     loaded_json = json.load(
#         open(translation_json_src)
#     )  # json opened and converted to dictionary for Python to understand
#     json_string = json.dumps(loaded_json, indent=4)  # stringified dictionary.

#     try:
#         translation = GoogleTranslator(
#             source=source_language, targetLanguage=target_language
#         ).translate(json_string)
#         Output_text.delete(1.0, END)
#         Output_text.insert(END, translation)
#     except Exception as e:
#         print(f"Translation error: {e}")
