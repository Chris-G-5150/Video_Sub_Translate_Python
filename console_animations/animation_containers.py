from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class BootSequences:
    app_init: Optional[Callable] | None = None
