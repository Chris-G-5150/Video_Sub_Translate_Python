# TODO - Create a main generator that injects the correct API class based on what has been selected

# TODO - Decide if the user should be choosing this, would it potentially be the case to set a default
#   that just sends the extracted audio to be quicker?

# TODO - Work out how to obscure and protect API keys, potentially get user to submit on starting the process based on
#  choice of generator.

# TODO - idea to consolidate some repetitive code ****potentially**** - think about what each API actually needs that
#   will be common ground between all of them, potentially make a master class that takes care of this, then just
#   separate what they need into functions on the more specific classes?
#   Look at options, could use the master class to call a function on the api_choice class which takes care of this,
#   making it more generic and easier to manage since all the specificity is taken care of on the individuals.

# API choice gets picked by user -> passes API key to the individual API class which creates a new instance,
# this then gets passed to the constructor of the Speech to text generator which takes care of all the processing,
# of the chunks and text of the audio, leaving the API classes just to do their job.

# Todo - Function to swap out API class based on user choice rather than creating a new instance, could get messy if
#   it starts re-processing the audio.

# Todo - look what each API needs to complete a call, get from docs.

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



# TODO - fill out later, maybe reduce the amount for demo purposes, more of a list of potential choices.

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