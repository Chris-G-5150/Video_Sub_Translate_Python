from functools import wraps

from event_handlers_and_data.base_event_types import EventStatus, StatusData


def emits(event_name: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # if called directly from event system
            if len(args) == 1 and isinstance(args[0], StatusData):
                event_data = args[0]
                print(f"[DEBUG] Received event data: {event_data}")
                return  # or handle as needed

            # otherwise it's a normal method call
            self = args[0]
            try:
                result = func(*args, **kwargs)
                self.events_dispatcher.trigger_event(
                    event_name, StatusData(EventStatus.OK, f"{event_name} completed successfully.")
                )
                return result
            except Exception as e:
                self.events_dispatcher.trigger_event(
                    event_name, StatusData(EventStatus.ERROR, f"{event_name} failed: {e}")
                )
                return None

        return wrapper

    return decorator
