import os

from pydub import AudioSegment, silence

import shutil
from pathlib import Path, PurePosixPath
from extracted_audio import ExtractedAudio
from speech_chunk import SpeechChunk
from compatible_audio_formats import CompatibleAudioFormats

#   Steps
# 1. Take full audio clip made in separate_audio_from_video to detect_audio_silence
# 2. Create global list to store clips, clips will be a dictionary with this form,
#   take these and piece by piece transcribe the audio,
# 3. Consolidate into classes for each platform depending on the above and dependency inject them into a class that
#       creates the final sub-title files.
#
#  TODO - Look up dependency injection in Python
#
# detect_audio_silence gets called to detect audio silence in extracted audio and  chop_on_silence will split based on parameters,
# this will create a global list of dictionaries where all the audio that isn't silent, is separated and passed to pydub.
# pydub will then go on to write the text from each stored audio file to each dictionary and then another part of the program will
# take care of the concatenating of the script for the dialogue and passing to the translator.
# TODO - Create class to deal with building the sub title files.
# Done - look at writing each clip to disk in a folder and play them back for testing.
#

class DetectAudioSilence:
    def __init__(
            self,
            extracted_audio: ExtractedAudio,
            user_silence_offset: float,
            user_silence_duration: int
    ):
        self.extracted_audio = extracted_audio
        self.user_silence_offset = user_silence_offset
        self.user_silence_duration = user_silence_duration

    def build_output_directory(self):
        if os.path.exists(self.extracted_audio.silence_removed_chunks_dir) and os.path.isdir(self.extracted_audio.silence_removed_chunks_dir):
            shutil.rmtree(self.extracted_audio.silence_removed_chunks_dir)

        Path(self.extracted_audio.silence_removed_chunks_dir).mkdir(parents=True, exist_ok=True)

    def get_audio_file_type(self):
        return CompatibleAudioFormats[PurePosixPath(self.extracted_audio.path_to_source_audio_file).suffix.replace('.', '').lower()] # <- lower guarantees this will always be correct

    def split_audio_remove_silence(self):
        self.extracted_audio.path_to_output_audio = PurePosixPath(self.extracted_audio.path_to_output_audio)
        audio_file_type = self.get_audio_file_type()
        audio = AudioSegment.from_file(self.extracted_audio.path_to_source_audio_file, audio_file_type)
        silence_threshold = audio.dBFS - self.user_silence_offset

        self.build_output_directory()

        speech_chunks = silence.split_on_silence(
        audio,
        min_silence_len = 1500,
        silence_thresh = silence_threshold,
        keep_silence = self.user_silence_duration,
        seek_step = 10
        )

        speech_chunks_silence_removed = []
        # Very doubtful actual speech sections will be less than two seconds, cuts out loud breathing/background sections
        for chunk in speech_chunks:
            if not chunk.duration_seconds < 2:
                speech_chunks_silence_removed.append(chunk)
        #   Filters speech chunks out less than 2 seconds long out before writing to disk, makes sure that the indexes are in
        #   the correct order for the sub files instead of having 1: some dialogue 2: **nothing** 3: some dialogue.
        #   This keeps sub files concise and no longer than they need to be.

        for index, chunk in enumerate(speech_chunks_silence_removed):
                print(f"Exporting chunk {index} ({len(chunk) / 1000:.2f}s)")
                path_to_chunk = PurePosixPath(self.extracted_audio.path_to_output_audio, f"{index}.mp3")
                chunk.export(path_to_chunk, format="mp3")
                audio_file_type = self.get_audio_file_type()
                # ^ mp3 keeps things small and quicker to pass to API not much of a loss for speech
                new_speech_chunk = SpeechChunk(
                    self.extracted_audio.project_title,
                    index,
                    path_to_chunk,
                    chunk.duration_seconds,
                    chunk.duration_seconds,
                    audio_file_type

                )

                self.extracted_audio.add_speech_chunk(new_speech_chunk)









