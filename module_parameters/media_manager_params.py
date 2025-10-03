from dataclasses import dataclass
from typing import Optional
from data_enums.iso_639_languages import ISO639Language

@dataclass
class MediaManagerParams:
    source_video_start_point: str = '00:00:00'
    user_silence_offset: int = 15
    user_silence_duration: int = 1500
    target_language: Optional[str | ISO639Language] = None
