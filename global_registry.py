from data_types_and_classes.data_constants import (
	CompatibleAudioFormats,
	CompatibleVideoFormats,
	CompletionStatus,
	StateSteps,
	StateStepsReference,
	TranscriptionPlatforms,
	WhisperEnglishModels,
	WhisperMultiLingualModels,
)
from data_types_and_classes.data_types import AppParams, Injectable, SpeechChunk, StateStep


		config = {
			"global_config": {},
			"app_params": {},
		}
		
		data_constants = {
			"compatible_audio_formats": CompatibleAudioFormats,
			"compatible_video_formats": CompatibleVideoFormats,
			"whisper_multi_ling_models": WhisperMultiLingualModels,
			"whisper_english_models": WhisperEnglishModels,
			"transcription_platforms": TranscriptionPlatforms,
			"completion_status": CompletionStatus,
			"state_steps_reference": StateStepsReference,
			"state_steps": StateSteps,
		}

		self.data_types = {
			"app_params": AppParams,
			"state_step": StateStep,
			"speech_chunk": SpeechChunk,
			"injectable": Injectable,
		}
