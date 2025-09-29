from audio_extract import extract_audio
import os
import main

# start time format is string HH:MM:SS
# duration is same format
# audio types passed as string in lower case['wav', 'ogg', 'mp3', 'aac', 'flac', 'm4a', 'oga', 'opus']
# video file extensions accepted ['mp4', 'mkv', 'webm', 'flv', 'avi', 'mov', 'wmv', 'm4v']
# compatible formats are in main.py, put into a class to encapsulate later.

def process_video_to_audio(path_of_video,
                           path_of_audio,
                           output_format='mp3',
                           start_time='00:00:00',
                           clip_duration=None):

    # Sends back a tuple of the path plus the extension (filepath, extension), hence [1]
    video_file_format = os.path.splitext(path_of_video)[1]

    # bools for creating error messages.
    audio_format_is_valid = output_format in main.audio_formats
    video_format_is_valid = video_file_format in main.video_formats
    both_formats_valid = audio_format_is_valid and video_format_is_valid

    if not both_formats_valid:
        raise ValueError('Invalid video and audio formats, please check compatibility')

    if not audio_format_is_valid or not video_format_is_valid:
        video = ("", "video")[video_format_is_valid]
        audio = ("", "audio")[audio_format_is_valid]
        raise ValueError(f"Invalid {video, audio} format, please check compatibility")

    else:
        extract_audio(input_path=path_of_video,
                      output_path=path_of_audio,
                      output_format=output_format,
                      start_time=start_time,
                      duration=clip_duration
                      )
        main.path_to_extracted_audio = path_of_audio # make a setter in a class once tested
        main.audio_file_extension = output_format # make a setter in a class once tested



