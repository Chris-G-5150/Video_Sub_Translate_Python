from enum import Enum


class TranscriptionPlatform(str, Enum):
	Google = "Google"
	WhisperAPI = "Whisper API"
	WhisperLocal = "Whisper Local"
	Wav2Vec2 = "Wav2Vec2"
	Vosk = "Vosk"
	NemoASR = "NemoASR"
	SpeechRecognition = "SpeechRecognition"
	CoquiSTT = "CoquiSTT"
	MozillaDeepSpeech = "MozillaDeepSpeech"
	SpeechD5 = "SpeechD5"

	@classmethod
	def has_value(cls, value: str) -> bool:
		return value in cls._value2member_map_

	def __str__(self) -> str:
		return self.value
