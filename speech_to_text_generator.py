class SpeechToTextGenerator:
    def __init__(self, speech_chunks, api_choice, source_language, target_language):
        self.speech_chunks = speech_chunks
        self.api_choice = api_choice
        self.speech_chunks = speech_chunks
        self.selected_language = source_language
        self.target_language = target_language


    # TODO - look up python API calls, just notes to figure out control flow.
    def process_speach_chunks(self):
        #    info object is what the API is expecting, most will probably need similar things, abstract as much as possible
        #    if anything out of the ordinary, get its own class to process and take care of it.
        #
        #    info_object = api_choice.get_info_object(pass the data it needs, hard code the specific info for each API
        #       inside it's respective class)

        #    self.postChunks(info_object)

    # Python has a bunch of calls
    # try:
    # except: TODO - look up exception types and what they do.
    # else:





class Google:
    def __init__(self, api_key):
        self.API_KEY = api_key


class Whisper:
    def __init__(self, api_key):
        self.API_KEY = api_key

class Wav2Vec2:
    def __init__(self, api_key):
        self.API_KEY = api_key

class Vosk:
    def __init__(self, api_key):
        self.API_KEY = api_key

class NemoASR:
    def __init__(self, api_key):
        self.API_KEY = api_key

class SpeechRecognition:
    def __init__(self, api_key):
        self.API_KEY = api_key

class CoquiSTT:
    def __init__(self, api_key):
        self.API_KEY = api_key

class MozillaDeepSpeech:
    def __init__(self, api_key):
        self.API_KEY = api_key

class SpeechD5:
    def __init__(self, api_key):
        self.API_KEY = api_key