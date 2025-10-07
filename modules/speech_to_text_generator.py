# from dataclasses import dataclass
# from typing import Optional
# from media_manager import ExtractedAudioAndVideoData
# from data_enums.iso_639_languages import ISO639Language, ISO3166Regions
# from data_classes.speech_chunk import SpeechChunk
# from data_enums.transcription_platform import TranscriptionPlatform
#
# # API
# # TODO - idea to consolidate some repetitive code ****potentially**** - think about what each API actually needs that
# #   will be common ground between all of them, potentially make a master class that takes care of this, then just
# #   separate what they need into functions on the more specific classes?
# #   Look at options, could use the master class to call a function on the transcription_platform class which takes care of this,
# #   making it more generic and easier to manage since all the specificity is taken care of on the individuals.
# #
# # Todo - Function to swap out API class based on user choice rather than creating a new instance, could get messy if
# #   it starts re-processing the audio.
# #
# # Todo - look what each API needs to complete a call, get from docs.
#
# @dataclass
# class APIParams:
#     api_key: str
#     get: str
#     post: str
#
#     transcription_platform: TranscriptionPlatform
#
# class API :
#     def __init__(self, params: APIParams):
#         self.API_KEY = params.api_key
#
#     def connect_to_api(self):
#         # check connection
#         # send back and okay message
#         # move to the next step with some try blocks, look up best practices in python
#
# @dataclass
# class SpeechToTextGeneratorParams:
#     extracted_audio_and_video_data: ExtractedAudioAndVideoData
#     silence_removed_speech_chunks: list[SpeechChunk]
#     transcription_platform: TranscriptionPlatform
#     transcription_platform_params:
#     source_language: Optional[ISO639Language]
#     target_language: Optional[ISO639Language]
#     source_language_dialect: Optional[ISO3166Regions] = None
#
# class SpeechToTextGenerator:
#     def __init__(self, params: SpeechToTextGeneratorParams, api: API):
#         self.silence_removed_speech_chunks = params.silence_removed_speech_chunks
#         self.transcription_platform = params.transcription_platform
#         self.selected_language = params.source_language
#         self.target_language = params.target_language
#         self.API = api
#
#     # def transcribe_speach_chunks(self, transcription_platform, source_language, target_language):
#
#
