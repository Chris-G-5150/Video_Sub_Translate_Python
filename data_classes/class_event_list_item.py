from typing import Type


class ClassEventListItem:
    def __init__(
        self, order: int, event_name: str, function_ref, class_ref: Type[any] | None = None
    ):
        self.order = (order,)
        self.event_name = event_name
        self.class_ref = class_ref | None
        self.function_ref = function_ref


# This will be for a much bgger machine which can offload a bunch of manual calls,
# the events themselves will be held within the classes with a classname.get_events_list() call like in data initialization
class AutomationProcessorListItem:
    def __init__(self, order: int, automated_class: Type[any], automated_class_params):
        self.automated_class = (automated_class,)
        self.automated_class_params = (automated_class_params)

AutomatedJobProcessor
 - gets the list items in their order
 - initializes the class, gives it it's params whilst passing a function to mark as complete 
 -	and move to the next item in the list could just be another EventStatus.OK, 
 - gets the eventlist from the class itself, 
 - initializes the sequential_event_processor per list item, 
 - gets all the tasks done that don't need interraction such as bulding data for the app and making folders etc. 