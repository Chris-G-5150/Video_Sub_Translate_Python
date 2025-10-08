from dataclasses import dataclass
from enum import Enum
from pathlib import Path

from data_classes.speech_chunk import SpeechChunk


@dataclass
class StateStep:
	step: int
	description: str
	speech_chunks_file_path: Path | None = None
	state_step_file_path: Path | None = None
	speech_chunks: list[SpeechChunk] | None = None
	completion_status: str | None = None
	state_written_to_disk: bool = False


class StateStepsReference(Enum):
	Start = "start"
	AudioExtracted = "audio_extracted"
	SpeechChunksSilenceRemoved = "speech_chunks_silence_removed"
	SpeechChunksSilence_Removed = "speech_chunks_silence_removed"
	SpeechChunksTranscriptionCompleted = "speech_chunks_transcription_completed"
	SpeechChunksSourceSubtitle = "speech_chunks_source_subtitle"
	SpeechChunksTranslationCompleted = "speech_chunks_translation_completed"
	SpeechChunksTranslatedSubtitle = "speech_chunks_translated_subtitle"
	AllOperationsCompleted = "all_operations_completed"
	

class StateSteps:
	def __init__(self):
		self.state_steps = {
			"start": StateStep(step=0, description="start", speech_chunks_file_path=None, speech_chunks=None),
			"audio_extracted": StateStep(
				step=1,
				description="audio_extracted",
				speech_chunks_file_path=None,
				speech_chunks=None,
			),
			"speech_chunks_silence_removed": StateStep(
				step=2,
				description="speech_chunks_silence_removed",
				speech_chunks_file_path=None,
				speech_chunks=None,
			),
			"speech_chunks_transcription_completed": StateStep(
				step=3,
				description="speech_chunks_transcription_completed",
				speech_chunks_file_path=None,
				speech_chunks=None,
			),
			"speech_chunks_source_subtitle": StateStep(
				step=4,
				description="speech_chunks_source_subtitle",
				speech_chunks_file_path=None,
				speech_chunks=None,
			),
			"speech_chunks_translation_completed": StateStep(
				step=5,
				description="speech_chunks_translation_completed",
				speech_chunks_file_path=None,
				speech_chunks=None,
			),
			"speech_chunks_translated_subtitle": StateStep(
				step=6,
				description="speech_chunks_translated_subtitle",
				speech_chunks_file_path=None,
				speech_chunks=None,
			),
			"all_operations_completed": StateStep(
				step=6,
				description="all_operations_complete",
				speech_chunks_file_path=None,
				speech_chunks=None,
			),
		}
	
		self.current_state_step = None
	
	def get_state_step(self, name_of_state):
		state_ref = evaluate_enum(name_of_state, StateStepsReference)
		return getattr(self.state_steps, state_ref)

	def set_current_state_step(self, name_of_state):
		state_ref = evaluate_enum(name_of_state, StateStepsReference)
		self.current_state_step = getattr(self.state_steps, state_ref)

	def update_current_state_step(self, name_of_state, properties_to_update: dict):
		state_ref = evaluate_enum(name_of_state, StateStepsReference)
		
		target = getattr(self.current_state_step, state_ref, None)
		if not target:
			return  # or raise an error if missing

		for change, new_value in properties_to_update.items():
        
			if target.get(change) is None:
				target[change] = new_value
					





