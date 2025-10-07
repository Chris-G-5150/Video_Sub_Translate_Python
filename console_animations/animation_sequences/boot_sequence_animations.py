import sys
import time

from console_animations.animation_containers import BootSequences


def app_init(console=None, delay: float = 0.5, char_delay: float = 0.015):
    if console and hasattr(console, "clear"):
        console.clear()

    lines = [
        "[SYSTEM] ACCESS: GRANTED",
        "[BOOT] Initializing cognitive layers...",
        "[CORE] Sync Ratio: 97.6%",
        "[NERV OS] Modules loading...",
        "[LCL] Interface stabilization complete.",
        "[READY] System online. Welcome, Commander.",
    ]

    for line in lines:
        for ch in line:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(char_delay)
        sys.stdout.write("\n")
        sys.stdout.flush()
        time.sleep(delay)

    sys.stdout.write("\n>> OPERATION START <<\n\n")
    sys.stdout.flush()


boot_sequences = BootSequences(
    app_init=app_init,
)
