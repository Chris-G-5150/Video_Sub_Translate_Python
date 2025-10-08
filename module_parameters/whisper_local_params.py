from dataclasses import dataclass
from typing import Optional

from data_enums.whisper_local_models import (
	WhisperEnglishModels,
	WhisperMultiLingualModels,
)
from modules.file_manager import FileManager
from modules.media_manager import MediaManager


@dataclass
class WhisperLocalParams:
	media_manager: MediaManager
	file_manager: FileManager
	chosen_model: Optional[str | WhisperEnglishModels] | Optional[str | WhisperMultiLingualModels]
