
from pathlib import Path


def build_file_os_path(app_base_dir, *parts: str | Path) -> Path:
	return app_base_dir.joinpath(*parts)