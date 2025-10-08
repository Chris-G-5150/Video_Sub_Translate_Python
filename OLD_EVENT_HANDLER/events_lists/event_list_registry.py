# from event_handlers_and_data.events_lists.app_initializer_events import AppEventListeners
# from event_handlers_and_data.events_lists.data_initializer_events import (
#     DataInitializerEventListeners,
# )
# from event_handlers_and_data.events_lists.file_manager_events import FileManagerEventListeners
# from event_handlers_and_data.events_lists.global_state_events import GlobalStateEventListeners


# def create_listener_dictionary(listener_list):
#     listener_list = {}
#     for value in listener_list:
#         listener_list[value] = value
#     print(listener_list)
#     return listener_list


# app_events = create_listener_dictionary(AppEventListeners.list())
# data_events = create_listener_dictionary(DataInitializerEventListeners.list())
# global_events = create_listener_dictionary(GlobalStateEventListeners.list())
# file_manager_events = create_listener_dictionary(FileManagerEventListeners.list())

# event_registry = {
#     "AppEventListeners": app_events,
#     "DataInitializerEventListeners": data_events,
#     "GlobalStateEventListeners": global_events,
#     "FileManagerEventListeners": file_manager_events,
# }
