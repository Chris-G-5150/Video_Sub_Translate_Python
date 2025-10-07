import random
from time import sleep

from rich.console import Console
from rich.live import Live
from rich.progress import Progress
from rich.table import Table
from rich.text import Text


class ConsoleAnimator:
    def __init__(self):
        self.console = Console()

        from console_animations.animation_sequences.boot_sequence_animations import (
            boot_sequences,
        )

        self.animations = {
            "boot_sequences": boot_sequences,
        }

    # --- Simple Evangelion-style header ---
    def show_banner(self, message: str):
        banner = Text(f"\n:: {message} ::", style="bold red on black", justify="center")
        self.console.rule(banner)

    # --- Generic progress animation ---
    def show_progress(self, title: str, duration: float = 2.0):
        with Progress(console=self.console, transient=True) as progress:
            task = progress.add_task(f"[green]{title}", total=100)
            for i in range(100):
                progress.update(task, advance=1)
                sleep(duration / 100)

    # --- Fancy “system scan” style animation ---
    def show_status_matrix(self, lines: int = 6, duration: float = 3.0):
        """Displays scrolling pseudo-data, NERV-style."""
        with Live(auto_refresh=False, console=self.console) as live:
            start = self.console.get_datetime()
            elapsed = 0.0
            while elapsed < duration:
                table = Table(show_header=False, box=None, style="bright_green")
                for _ in range(lines):
                    rand_bits = "".join(random.choice("01") for _ in range(48))
                    table.add_row(rand_bits)
                live.update(table, refresh=True)
                sleep(0.1)
                elapsed = (self.console.get_datetime() - start).total_seconds()

    def notify_complete(self, message: str):
        self.console.print(f"[bold red]{message}[/bold red]")

    def play(self, container_name: str, animation_name: str, **kwargs):
        container = self.animations.get(container_name)
        if not container:
            print(f"[ConsoleAnimator] Unknown container: {container_name}")
            return None

        animation_func = getattr(container, animation_name, None)
        if not callable(animation_func):
            print(f"[ConsoleAnimator] Invalid animation reference: {animation_name}")
            return None

        return animation_func(**kwargs)
