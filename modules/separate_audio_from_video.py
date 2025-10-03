from dataclasses import dataclass
from audio_extract import extract_audio
from data_enums.compatible_audio_formats import CompatibleAudioFormats
from data_enums.compatible_video_formats import CompatibleVideoFormats
from modules.file_manager import FileManager
from modules.media_manager import MediaManager

@dataclass
class SeparateAudioFromVideoParams:
    media_manager: MediaManager
    file_manager: FileManager

class SeparateAudioFromVideo:
    def __init__(self, params: SeparateAudioFromVideoParams):
        self.media_manager = params.media_manager
        self.file_manager = params.file_manager
        self.process_step = "1"

    def process_video_to_audio(self) -> str:
        media_manager = self.media_manager
        file_manager = self.file_manager
        directories = file_manager.directories
        audio_format = media_manager.extracted_audio_format
        audio_format_is_valid = CompatibleAudioFormats.has_value(audio_format)
        video_format_is_valid = CompatibleVideoFormats.has_value(media_manager.source_video_format)
        both_formats_valid = audio_format_is_valid and video_format_is_valid

        audio_output_path = file_manager.build_file_os_path(file_manager.directories.extracted_audio_dir, f"{media_manager.project_title}-extractedaudio.{audio_format}")

        if not both_formats_valid:
            raise ValueError('Invalid video and audio formats, please check compatibility')

        if not audio_format_is_valid or not video_format_is_valid:
            video = ("", "video")[video_format_is_valid]
            audio = ("", "audio")[audio_format_is_valid]
            raise ValueError(f"Invalid {video, audio} format, please check compatibility")

        else:
            extract_audio(
                input_path=str(directories.video_file_path),
                output_path=str(audio_output_path),
                output_format=str(media_manager.extracted_audio_format),
                start_time=str(media_manager.source_video_start_point),
                duration=None
            )

            file_manager.extracted_audio_path = audio_output_path

            return 'Complete'










