from enum import Enum
audio_formats = ['wav', 'ogg', 'mp3']
video_formats = ['mp4', 'mkv', 'webm', 'flv', 'avi', 'mov', 'wmv', 'm4v']

class TranscriptionPlatform(Enum):
    Google = 'Google'
    WhisperAPI = 'Whisper API'
    WhisperLocal = 'Whisper Local'
    Wav2Vec2 = 'Wav2Vec2'
    Vosk = 'Vosk'
    NemoASR = 'NemoASR'
    SpeechRecognition = 'SpeechRecognition'
    CoquiSTT = 'CoquiSTT'
    MozillaDeepSpeech = 'MozillaDeepSpeech'
    SpeechD5 = 'SpeechD5'

path_to_extracted_audio = ''
audio_file_extension = ''
audio_slices = []

# Whisper Local
# TODO - turns out OpenAI's whisper can be installed locally as well as be called from an API, in that case to save on time
#   will insall this locally into the project to see how it fairs, will also have APIs available if results aren't satisfactory.


# TODO - fill out later, maybe reduce the amount for demo purposes, more of a list of potential choices.

# TODO - Create a main generator that injects the correct API class based on what has been selected

# TODO - Decide if the user should be choosing this, would it potentially be the case to set a default
#   that just sends the extracted audio to be quicker?

# TODO - Work out how to obscure and protect API keys, potentially get user to submit on starting the process based on
#  choice of generator.


# API
# TODO - idea to consolidate some repetitive code ****potentially**** - think about what each API actually needs that
#   will be common ground between all of them, potentially make a master class that takes care of this, then just
#   separate what they need into functions on the more specific classes?
#   Look at options, could use the master class to call a function on the api_choice class which takes care of this,
#   making it more generic and easier to manage since all the specificity is taken care of on the individuals.
#
# Todo - Function to swap out API class based on user choice rather than creating a new instance, could get messy if
#   it starts re-processing the audio.
#
# Todo - look what each API needs to complete a call, get from docs.


# Language compatibility
# TODO - investigate further if there are some that take triple character country codes.