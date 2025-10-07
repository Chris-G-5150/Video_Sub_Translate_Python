import json
from pathlib import Path
from data_classes.global_config import GlobalConfig
from data_classes.speech_chunk import SpeechChunk
from data_classes.state_steps import StateStep


class JsonUtils:
    def __init__(self, global_config: GlobalConfig):
        self.global_config = None

    def get_speech_chunk_json_file_name(self, state_step: StateStep):
        return f"{state_step.step}-{self.global_config.project_title}-{state_step.description}"

    @staticmethod
    def convert_state_step_to_json(state_step: StateStep) -> str:
        return json.dumps(state_step, indent=4)

    @staticmethod
    def from_json_to_dict(path: str | Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def dict_to_speech_step(self, path: str | Path) -> StateStep:
        state_step_dict = self.from_json_to_dict(path)
        chunks = [
            SpeechChunk(**chunk) for chunk in state_step_dict.get("speech_chunks", [])
        ]
        return StateStep(
            step=state_step_dict["step"],
            description=state_step_dict["description"],
            speech_chunks=chunks,
            state_step_file_path=state_step_dict["state_step_file_path"],
            speech_chunks_file_path=state_step_dict["speech_chunks_file_path"],
        )
