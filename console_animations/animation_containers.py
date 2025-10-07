from dataclasses import dataclass
from typing import Optional, Callable


@dataclass
class BootSequences:
    app_init: Optional[Callable] | None = None
