from data_classes.global_state import ClassInitializationStatus
from modules.console_animator import ConsoleAnimator


class ModuleInitializer:
    def __init__(self, app_class_props, console_animator: ConsoleAnimator | None = None):
        self.console_animator = console_animator or ConsoleAnimator()
        self.class_initialization_status = ClassInitializationStatus()
