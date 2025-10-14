from data_types_and_classes.data_types import StateStep
from helper_classes import DotDict

CompatibleAudioFormats = DotDict({
	"WAV": "wav",
	"OGG": "ogg",
	"MP3": "mp3",
})

CompatibleVideoFormats = DotDict({
	"MP4": "mp4",
	"MKV": "mkv",
	"WEBM": "webm",
	"FLV": "flv",
	"AVI": "avi",
	"MOV": "mov",
	"WMV": "wmv",
	"M4V": "m4v",
})

WhisperMultiLingualModels = DotDict({
	"Tiny": "tiny",
	"Base": "base",
	"Small": "small",
	"Medium": "medium",
	"Large": "large",
	"Turbo": "turbo",
})

WhisperEnglishModels = DotDict({
	"TinyEn": "tiny.en",
	"BaseEn": "base.en",
	"SmallEn": "small.en",
	"MediumEn": "medium.en",
})

TranscriptionPlatforms = DotDict({
	"Google": "Google",
	"WhisperAPI": "Whisper API",
	"WhisperLocal": "Whisper Local",
	"Wav2Vec2": "Wav2Vec2",
	"Vosk": "Vosk",
	"NemoASR": "NemoASR",
	"SpeechRecognition": "SpeechRecognition",
	"CoquiSTT": "CoquiSTT",
	"MozillaDeepSpeech": "MozillaDeepSpeech",
	"SpeechD5": "SpeechD5",
})

CompletionStatus = DotDict({
	"Error": "ERROR",
	"Complete": "COMPLETE",
	"InProgress": "IN PROGRESS",
	"NotStarted": "NOT_STARTED",
})

StateStepsReference = DotDict({
	"Start": "start",
	"BuildGlobalConfig": "build_global_config",
	"CreateDirectoriesInFileSystem": "build_global_config",
	"AudioExtracted": "audio_extracted",
	"SpeechChunksSilenceRemoved": "speech_chunks_silence_removed",
	"SpeechChunksSilence_Removed": "speech_chunks_silence_removed",
	"SpeechChunksTranscriptionCompleted": "speech_chunks_transcription_completed",
	"SpeechChunksSourceSubtitle": "speech_chunks_source_subtitle",
	"SpeechChunksTranslationCompleted": "speech_chunks_translation_completed",
	"SpeechChunksTranslatedSubtitle": "speech_chunks_translated_subtitle",
	"AllOperationsCompleted": "all_operations_completed",
	"WritingGlobalConfigToDisk": "writing_global_config_to_disk",
	"WritingSpeechChunksToDisk": "writing_speech_chunk_to_disk",
})

StateSteps = DotDict({
	f"{StateStepsReference.Start}": StateStep(
		step_name="start",
		description="Starting app, preparing data",
	),
	f"{StateStepsReference.BuildGlobalConfig}": StateStep(
		step_name="build_global_config",
		description="Building GlobalConfig",
	),
	f"{StateStepsReference.CreateDirectoriesInFileSystem}": StateStep(
		step_name="create_directories_in_file_system",
		description="Creating directories in file system",
	),
	f"{StateStepsReference.AudioExtracted}": StateStep(
		step_name="audio_extracted",
		description="Audio being extracted from video",
	),
	f"{StateStepsReference.WritingGlobalConfigToDisk}": StateStep(
		step_name="writing_global_config_to_disk",
		description="Writing GlobalConfig to disk",
	),
	f"{StateStepsReference.SpeechChunksSilenceRemoved}": StateStep(
		step_name="speech_chunks_silence_removed",
		description="Audio, removing silence and building SpeechChunk list.",
	),
	f"{StateStepsReference.SpeechChunksTranscription}": StateStep(
		step_name="speech_chunks_transcription_completed",
		description="Source language transcription being made",
	),
	f"{StateStepsReference.SpeechChunksSourceSubtitle}": StateStep(
		step_name="speech_chunks_source_subtitle",
		description="Source language subtitle file being built",
	),
	f"{StateStepsReference.SpeechChunksTranslation}": StateStep(
		step_name="speech_chunks_translation_completed",
		description="SpeechChunks being translated",
	),
	f"{StateStepsReference.SpeechChunksTranslatedSubtitle}": StateStep(
		step_name="speech_chunks_translated_subtitle",
		description="Translated language subtitle file being built",
	),
	f"{StateStepsReference.AllOperationsCompleted}": StateStep(
		step_name="all_operations_complete",
		description="All operations complete, now you can use the files in any video editor",
	),
})
