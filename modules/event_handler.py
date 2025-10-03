from dataclasses import dataclass
from enum import Enum

class EventStatus(Enum):
    Okay = 'Okay'
    Error = 'Error'

@dataclass
class TriggerEvent:
    action: str

class EventHandler:
    def __init__(self):
        self.listeners = []

    def add_listener(self, listener):
        self.listeners.append(listener)

    def remove_listener(self, listener):
        if listener in self.listeners:
            self.listeners.remove(listener)

    def trigger_event(self, event_data=None):
        for listener in self.listeners:
            listener(event_data)

# TODO - Put paths to where the files are located in every print out

@dataclass
class StatusData:
    status: str | EventStatus
    status_message: str = ''

def separate_audio_from_video_complete(status_data: StatusData) -> bool:
    if status_data.status == EventStatus.Error:
        print("Separation of audio from video:", status_data.status_message)
        return False
    else:
        print("Separation of audio from video:", status_data.status_message)
        return True

def separate_and_remove_silence_from_audio_complete(status_data: StatusData) -> bool:
    if status_data.status == EventStatus.Error:
        print("Separate and remove silence from audio:", status_data.status_message)
        return False
    else:
        print("Separate and remove silence from audio:", status_data.status_message)
        return True

def speech_to_text_generator_complete(status_data: StatusData) -> bool:
    if status_data.status == EventStatus.Error:
        print("Speech to text generation:", status_data.status_message)
        return False
    else:
        print("Speech to text generation:", status_data.status_message)
        return True



#dispatcher = EventHandler()
#dispatcher.add_listener(my_listener)
#dispatcher.trigger_event("Hello, World!")


