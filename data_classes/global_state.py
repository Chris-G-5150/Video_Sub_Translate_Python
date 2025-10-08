from dataclasses import dataclass


@dataclass
class ClassInitializationStatus:
	data_initializer_initialized: bool = False
	speech_chunk_manager_initialized: bool = False
	event_handler_initialized: bool = False
	utils_class_initialized: bool = False
	json_utils_class_initialized: bool = False
	separate_and_remove_audio_silence_initialized: bool = False
	separate_audio_from_video_initialized: bool = False
	whisper_local_intialized: bool = False
	google_translate_initialized: bool = False
