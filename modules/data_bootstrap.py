from pathlib import Path

from data_types_and_classes.data_constants import CompatibleAudioFormats, CompatibleVideoFormats
from data_types_and_classes.data_types import AppParams
from data_types_and_classes.iso_639_languages import ISO639Language
from helper_classes import DotDict


def build_and_set_global_config(app_base_dir, app_params: AppParams):
	ap = app_params

	media_data = init_media_data(
		extracted_audio_format=ap.extracted_audio_format,
		source_video_format=ap.source_video_format,
		target_language=ap.target_language,
		source_video_file_name=ap.source_video_file_name,
		source_language=ap.source_language,
		source_language_dialect=ap.source_language_dialect
	)
	audio_extraction_config = init_audio_extraction_config(
		source_video_start_point=ap.source_video_start_point,
		user_silence_offset=ap.user_silence_offset,
		user_silence_duration=ap.user_silence_duration
	)
	app_directories = init_app_directories(app_base_dir=app_base_dir, project_title=ap.project_title),
	base_file_names = init_base_file_names(project_title=ap.project_title,
										   source_language=app_params.source_language,
										   target_language=app_params.target_language)
	app_paths_to_files = init_app_paths_to_files()
	
	global_config = DotDict({
		"project_title": ap.project_title,
		"media_data": media_data,
		"audio_extraction_config": audio_extraction_config,
		"app_directories": app_directories,
		"base_file_names": base_file_names,
		"app_paths_to_files": app_paths_to_files,
		"whisper_local_chosen_model": ap.whisper_local_chosen_model,
	})


def init_app_paths_to_files(app_base_dir=str, source_video_file_name=str) -> set[Path | None]:
	return build_app_paths_to_files_dict(
		video_file_path=build_file_os_path(app_base_dir, source_video_file_name),
		audio_from_video_path=None,
		transcription_source_language_paths=None,
		transcription_translated_language_dir=None,
	)


def init_app_directories(app_base_dir, project_title):
	# put all of these files in file manager.
	project_folder_dir = build_file_os_path(app_base_dir, project_title)
	
	return build_app_directories_dict(
		app_base_dir=app_base_dir,
		project_folder_dir=project_folder_dir,
		extracted_audio_dir=build_file_os_path(project_folder_dir, "extracted_audio"),
		silence_removed_chunks_dir=build_file_os_path(
			project_folder_dir, "silence_removed_audio"
		),
		transcription_source_language_dir=build_file_os_path(
			project_folder_dir, "transcription_source"
		),
		transcription_translated_language_dir=build_file_os_path(
			project_folder_dir, "transcription_translated"
		),
		speech_chunk_json_dir=build_file_os_path(
			project_folder_dir, app_params.project_title, "speech_chunk_data"
		),
		global_config_json_dir=build_file_os_path(
			project_folder_dir, project_title, "global_config_json"
		),
		global_state_json_dir=build_file_os_path(
			project_folder_dir, project_title, "global_state_json"
		),
	)


def init_media_data(extracted_audio_format: str, source_video_format: str, target_language: str,
					source_video_file_name: str, source_language: str, source_language_dialect: str):
	return build_media_data_dict(
		extracted_audio_format=CompatibleAudioFormats[f"{extracted_audio_format}"],
		source_video_format=CompatibleVideoFormats[f"{source_video_format}"],
		target_language=f"{target_language}",
		source_video_file_name=source_video_file_name,
		source_language=source_language,
		source_language_dialect=source_language_dialect
	)


def init_audio_extraction_config(source_video_start_point, user_silence_offset, user_silence_duration):
	return build_audio_extraction_config_dict(
		source_video_start_point=source_video_start_point,
		user_silence_offset=user_silence_offset,
		user_silence_duration=user_silence_duration,
	)


def init_base_file_names(project_title: str, source_language: ISO639Language, target_language: ISO639Language):
	pt = project_title
	return build_base_file_names_dict(
		global_state_json_file_name=f"{pt}-global-state-for-restore",
		transcription_source_language_file_name=f"{pt}whisper-transcription-{source_language}",
		speech_chunk_json_file_name=f"{pt}-speech-chunks-data",
		speech_chunk_audio_file_name=f"{pt}-silence-removed-clip-",
		extracted_audio_file_name=f"{pt}-extracted-from-video",
		transcription_text_filename=f"{pt}-whisper-transcription",
		transcription_translated_text_filename=f"{pt}-transcription-{source_language}",
		sub_source_language_file_name=f"{pt}-subtitle-{source_language}",
		sub_target_language_file_name=f"{pt}-subtitle-{target_language}",
	)


@staticmethod
def build_app_directories_dict(
		app_base_dir: Path,
		project_folder_dir: Path,
		extracted_audio_dir: Path,
		silence_removed_chunks_dir: Path,
		transcription_source_language_dir: Path,
		transcription_translated_language_dir: Path,
		speech_chunk_json_dir: Path,
		global_config_json_dir: Path,
		global_state_json_dir: Path,
):
	return {
		app_base_dir,
		project_folder_dir,
		extracted_audio_dir,
		silence_removed_chunks_dir,
		transcription_source_language_dir,
		transcription_translated_language_dir,
		speech_chunk_json_dir,
		global_config_json_dir,
		global_state_json_dir,
	}


@staticmethod
def build_app_paths_to_files_dict(
		video_file_path: Path | None,
		audio_from_video_path: Path | None,
		transcription_source_language_paths: Path | None,
		transcription_translated_language_dir: Path | None,
):
	return {
		video_file_path,
		audio_from_video_path,
		transcription_source_language_paths,
		transcription_translated_language_dir,
	}


@staticmethod
def build_audio_extraction_config_dict(
		source_video_start_point: str, user_silence_offset: int, user_silence_duration: int
):
	return {
		source_video_start_point,
		user_silence_offset,
		user_silence_duration,
	}


@staticmethod
def build_media_data_dict(
		extracted_audio_format: str,
		source_video_format: str,
		target_language: str,
		source_video_file_name: str,
		source_language: str,
		source_language_dialect: str,
):
	return {
		extracted_audio_format,
		source_video_format,
		target_language,
		source_video_file_name,
		source_language,
		source_language_dialect,
	}


@staticmethod
def build_base_file_names_dict(
		global_state_json_file_name,
		transcription_source_language_file_name,
		speech_chunk_audio_file_name,
		speech_chunk_json_file_name,
		extracted_audio_file_name,
		transcription_text_filename,
		transcription_translated_text_filename,
		sub_source_language_file_name,
		sub_target_language_file_name,
):
	return {
		global_state_json_file_name,
		transcription_source_language_file_name,
		speech_chunk_audio_file_name,
		speech_chunk_json_file_name,
		extracted_audio_file_name,
		transcription_text_filename,
		transcription_translated_text_filename,
		sub_source_language_file_name,
		sub_target_language_file_name,
	}


@staticmethod
def build_global_config_dict(
		project_title,
		media_data,
		audio_extraction_config,
		app_directories,
		base_file_names,
		app_paths_to_files,
		whisper_local_chosen_model,
):
	return {
		project_title,
		media_data,
		audio_extraction_config,
		app_directories,
		base_file_names,
		app_paths_to_files,
		whisper_local_chosen_model,
		base_file_names,
	}