from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from data_enums.compatible_audio_formats import CompatibleAudioFormats
from data_enums.iso_639_languages import ISO639Language


@dataclass
class SpeechChunk:
    project_title: str
    clip_srt_index: int
    speech_chunk_path: Path
    milisecond_start: int
    milisecond_end: int
    duration_in_miliseconds: int
    audio_format: str | CompatibleAudioFormats
    source_language: str | ISO639Language
    transcription_file_path: Optional[Path] | None = None
    transcription_source_language_path: Optional[Path] | None = None
    transcription_target_language_path: Optional[Path] | None = None
    transcription_source_language_text: str | None = None
    transcription_target_language_text: str | None = None
