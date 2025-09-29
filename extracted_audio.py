from pathlib import Path, PurePosixPath

from compatible_audio_formats import CompatibleAudioFormats
from speech_chunk import SpeechChunk

class ExtractedAudio:
    def __init__(self, project_title: str, path_to_source_audio_file: PurePosixPath, silence_removed_chunks_dir: PurePosixPath, audio_file_type: CompatibleAudioFormats):
        self.project_title = project_title
        self.path_to_source_audio_file = path_to_source_audio_file
        self.silence_removed_chunks_dir = silence_removed_chunks_dir
        self.audio_file_type = audio_file_type
        self.speech_chunks: list[SpeechChunk] = []

    def add_speech_chunk(self, speech_chunk: SpeechChunk):
        self.speech_chunks.append(speech_chunk)

    def get_speech_chunks(self) -> list[SpeechChunk]:
        return self.speech_chunks

    def clear_speech_chunks(self):
        self.speech_chunks = []




