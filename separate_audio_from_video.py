from pathlib import PurePosixPath
from audio_extract import extract_audio
import os
import main
from compatible_audio_formats import CompatibleAudioFormats
from compatible_video_formats import CompatibleVideoFormats
from extracted_audio import ExtractedAudio

# start time format is string HH:MM:SS
# duration is same format
# audio types passed as string in lower case['wav', 'ogg', 'mp3', 'aac', 'flac', 'm4a', 'oga', 'opus']
# video file extensions accepted ['mp4', 'mkv', 'webm', 'flv', 'avi', 'mov', 'wmv', 'm4v']
# compatible formats are in main.py, put into a class to encapsulate later.
class SeparateAudioFromVideo:
    def __init__(self,
                 project_title: str,
                 input_path: PurePosixPath,
                 input_start_time: str = "00:00:00",
                 output_audio_path: PurePosixPath = PurePosixPath("exported_segments"),
                 output_format: CompatibleAudioFormats = CompatibleAudioFormats['mp3']
                 ):
        self.project_title = project_title
        self.input_path = input_path
        self.input_start_time = input_start_time
        self.output_audio_path = output_audio_path
        self.output_format = output_format
        self.video_file_format = None
        self.extracted_audio = None

    def process_video_to_audio(self):
        self.video_file_format = PurePosixPath(self.input_path).suffix

        # bools for creating error messages.
        audio_format_is_valid = self.output_format in CompatibleAudioFormats
        video_format_is_valid = self.video_file_format in CompatibleVideoFormats
        both_formats_valid = audio_format_is_valid and video_format_is_valid

        if not both_formats_valid:
            raise ValueError('Invalid video and audio formats, please check compatibility')

        if not audio_format_is_valid or not video_format_is_valid:
            video = ("", "video")[video_format_is_valid]
            audio = ("", "audio")[audio_format_is_valid]
            raise ValueError(f"Invalid {video, audio} format, please check compatibility")

        else:
            extract_audio(input_path=str(self.input_path), output_path=str(self.output_audio_path),
                        output_format=str(self.output_format), start_time=self.input_start_time, duration=None)

            extracted_audio = ExtractedAudio(self.project_title, self.input_path, self.output_audio_path)






