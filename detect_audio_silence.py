from pydub import AudioSegment, silence, playback
import os
import shutil
from pathlib import Path


#   Steps
# 1. Take full audio clip made in separate_audio_from_video to detect_audio_silence
# 2. Create global list to store clips, clips will be a dictionary with this form,
#   take these and piece by piece transcribe the audio,
# 3. Consolidate into classes for each platform depending on the above and dependency inject them into a class that
#       creates the final sub-title files.
#
#  TODO - Look up dependency injection in Python
#
#
#
#
# detect_audio_silence gets called to detect audio silence in extracted audio and  chop_on_silence will split based on parameters,
# this will create a global list of dictionaries where all the audio that isn't silent, is separated and passed to pydub.
# pydub will then go on to write the text from each stored audio file to each dictionary and then another part of the program will
# take care of the concatenating of the script for the dialogue and passing to the translator.
# TODO - Create class to deal with building the sub title files.
#
#
#
# Done - look at writing each clip to disk in a folder and play them back for testing.

def build_output_directory(path_to_output: Path):
    if path_to_output.exists() and path_to_output.is_dir():
        shutil.rmtree(path_to_output)

    path_to_output.mkdir(parents=True, exist_ok=True)

def get_audio_file_type(path_to_file):
    return os.path.splitext(path_to_file)[1].replace('.', '').lower() # <- lower guarantees this will always be correct

def split_audio_remove_silence(path_to_file: str, path_to_output: str, user_silence_offset):
    path_to_output = Path(path_to_output)
    audio_file_type = get_audio_file_type(path_to_file)
    audio = AudioSegment.from_file("corry.mp3", audio_file_type)
    silence_threshold = audio.dBFS - user_silence_offset

    build_output_directory(path_to_output)

    speech_chunks = silence.split_on_silence(
    audio,
    min_silence_len=1500,
    silence_thresh=silence_threshold,
    keep_silence=500,
    seek_step=10
    )

    speech_chunks_silence_removed = []

    for index, chunk in enumerate(speech_chunks):
        if not chunk.duration_seconds < 2: # potentially filter these out beforehand? Will keep the files in order and consistent.
            #  ^ very doubtful actual speech sections will be less than two seconds, cuts out loud breathing/background
            print(f"Exporting chunk {index} ({len(chunk) / 1000:.2f}s)")
            chunk.export(os.path.join(path_to_output, f"{index}.mp3"), format="mp3") # <- mp3 keeps things small not much of a loss for speech



split_audio_remove_silence('corry.mp3', './exported_segments', 15)






