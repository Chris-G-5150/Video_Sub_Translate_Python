from dataclasses import dataclass
from pathlib import Path
from typing import List
from data_classes.speech_chunk import SpeechChunk

@dataclass
class StateStep:
    step: int
    description: str
    speech_chunks_file_path: Path | None = None
    speech_chunks: List[SpeechChunk] | None = None

@dataclass
class StateSteps:
    audio_extracted: StateStep
    speech_chunks_silence_removed: StateStep
    speech_chunks_transcription_completed: StateStep
    speech_chunks_source_subtitle: StateStep
    speech_chunks_translation_completed: StateStep
    speech_chunks_translated_subtitle: StateStep

#the speech chunks will be the path of where they are saved to as opposed to a reference as their may be issues with just referencing them 
state_steps = StateSteps(
    audio_extracted = StateStep(step=1, description="audio_extracted", speech_chunks_file_path=None, speech_chunks=None),
    speech_chunks_silence_removed = StateStep(step=2, description="speech_chunks_silence_removed", speech_chunks_file_path=None, speech_chunks=None),
    speech_chunks_transcription_completed = StateStep(step=3, description="speech_chunks_transcription_completed", speech_chunks_file_path=None, speech_chunks=None),
    speech_chunks_source_subtitle= StateStep(step=4, description="speech_chunks_source_subtitle", speech_chunks_file_path=None, speech_chunks=None),
    speech_chunks_translation_completed= StateStep(step=5, description="speech_chunks_translation_completed", speech_chunks_file_path=None, speech_chunks=None),
    speech_chunks_translated_subtitle= StateStep(step=6, description="speech_chunks_translated_subtitle", speech_chunks_file_path=None, speech_chunks=None),
)