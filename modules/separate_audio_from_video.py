from audio_extract import extract_audio

from data_classes.global_config import GlobalConfig
from data_enums.compatible_audio_formats import CompatibleAudioFormats
from data_enums.compatible_video_formats import CompatibleVideoFormats
from modules.utils import Utils


class SeparateAudioFromVideo:
	def __init__(self, global_config: GlobalConfig, utils: Utils):
		self.project_title = global_config.project_title
		self.directories = global_config.app_directories
		self.media_data = global_config.media_data
		self.audio_config = global_config.audio_extraction_config
		self.file_paths = global_config.app_paths_to_files
		self.audio_output_path = None
		self.utils = utils

	def process_video_to_audio(self) -> str:
		media_data = self.media_data
		directories = self.directories
		file_paths = self.file_paths
		audio_config = self.audio_config
		utils = self.utils
		audio_format_is_valid = CompatibleAudioFormats.has_value(media_data.extracted_audio_format)
		video_format_is_valid = CompatibleVideoFormats.has_value(media_data.source_video_format)
		both_formats_valid = audio_format_is_valid and video_format_is_valid

		audio_output_path = utils.build_file_os_path(
			directories.extracted_audio_dir, f"{self.project_title}-extractedaudio"
		).with_suffix(f"{media_data.extracted_audio_format}")

		if not both_formats_valid:
			raise ValueError("Invalid video and audio formats, please check compatibility")

		if not audio_format_is_valid or not video_format_is_valid:
			video = ("", "video")[video_format_is_valid]
			audio = ("", "audio")[audio_format_is_valid]
			raise ValueError(f"Invalid {video, audio} format, please check compatibility")

			# ********Confirmed the audio and video are valid formats******
			# Want a listener here to trigger the extract audio part that will be a separate function

		def extract_audio_to_dis():
			extract_audio(
				input_path=str(file_paths.video_file_path),
				output_path=str(audio_output_path),
				output_format=str(media_data.extracted_audio_format),
				start_time=str(audio_config.source_video_start_point),
				duration=None,
			)
			# ***** also a listener here to say that this is complete that will trigger the global config to be updated elsewhere
			self.audio_from_video_path = audio_output_path

			# ***** listener to see that this has been completed
			return "Complete"
