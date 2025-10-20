from data_classes.speech_chunk import SpeechChunk
from pydub import AudioSegment, silence


class SeparateAndRemoveAudioSilience:
	def __init__(self, global_config: GlobalConfig):
		self.project_title = global_config.project_title
		self.media_data = global_config.media_data
		self.directories = global_config.app_directories
		self.paths = global_config.app_paths_to_files
		self.user_silence_offset = global_config.audio_extraction_config.user_silence_offset
		self.user_silence_duration = global_config.audio_extraction_config.user_silence_duration,
		self.source_language = global_config.media_data.source_language,
		self.source_language_dialect = global_config.media_data.source_language_dialect,
		self.state_step = global_config.state_steps.audio_extracted
	
	def create_speech_chunks(self):
		directories = self.directories
		media_data = self.media_data
		paths = self.paths
		audio_format = media_data.extracted_audio_format
		extracted_audio_path = paths.audio_from_video_path
		audio_segment = AudioSegment.from_file(extracted_audio_path, audio_format)
		silence_threshold = audio_segment.dBFS - self.user_silence_offset
		output_directory = directories.silence_removed_chunks_dir
		
		speech_chunks = silence.split_on_silence(
			audio_segment,
			min_silence_len = 1500,
			silence_thresh = silence_threshold,
			keep_silence = self.user_silence_duration,
			seek_step = 10,
		)
		
		speech_chunks_silence_removed = []
		# Very doubtful actual speech sections will be less than two seconds, cuts out loud breathing/background sections
		for chunk in speech_chunks:
			if not chunk.duration_seconds < 2:
				speech_chunks_silence_removed.append(chunk)
		#   Filters speech chunks out less than 2 seconds long out before writing to disk, makes sure that the indexes are in
		#   the correct order for the sub files instead of having 1: some dialogue 2: **nothing** 3: some dialogue.
		#   This keeps sub files concise and no longer than they need to be.
		
		time_accumulator = 0.0
		
		for index, chunk in enumerate(speech_chunks_silence_removed):
			print(f"Exporting chunk {index} ({len(chunk) / 1000:.2f}s)")
			start_point_seconds = time_accumulator + 0.1
			end_point_seconds = start_point_seconds + chunk.duration_seconds
			
			chunk_file_path = file_manager.build_file_os_path(
				directories.silence_removed_chunks_dir,
				f"{index}-{app_params.project_title}-silence_removbed_chunk.{audio_format}",
			)
			
			new_speech_chunk = SpeechChunk(
				project_title = self.project_title,
				clip_srt_index = index,
				speech_chunk_path = chunk_file_path,
				duration_in_miliseconds = int(chunk.duration_seconds / 1000),
				milisecond_start = int(start_point_seconds / 1000),
				milisecond_end = int(end_point_seconds / 1000),
				audio_format = audio_format,
				source_language = media_data.source_language,
			)
			
			utilities.write_speech_chunk_to_disk(
				segment = audio_segment,
				chunk = new_speech_chunk,
				chunk_file_path = chunk_file_path,
			)
			self.media_manager.add_speech_chunk(new_speech_chunk)
		
		return "Complete"