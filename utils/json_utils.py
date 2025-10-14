import json
from pathlib import Path

from data_types_and_classes.data_types import SpeechChunk
from data_types_and_classes.state_steps import StateStep


def get_speech_chunk_json_file_name(project_title, state_step_name, state_step_order_number):
	return f"{project_title}-speech_chunks-{state_step_order_number}-{state_step_name}"


def convert_state_step_to_json(state_step: StateStep) -> str:
	return json.dumps(state_step, indent=4)


def from_json_to_dict(path: str | Path):
	if isinstance(path, Path):
		return json.loads(path.read_text(encoding="utf-8"))
	else:
		path_to_path = Path(path)
		json.loads(path_to_path.read_text(encoding="utf-8"))


def dict_to_speech_step(self, path: str | Path) -> StateStep:
	state_step_dict = self.from_json_to_dict(path)
	chunks = [SpeechChunk(**chunk) for chunk in state_step_dict.get("speech_chunks", [])]
	return StateStep(
		step=state_step_dict["step"],
		description=state_step_dict["description"],
		speech_chunks=chunks,
		state_step_file_path=state_step_dict["state_step_file_path"],
		speech_chunks_file_path=state_step_dict["speech_chunks_file_path"],
	)
