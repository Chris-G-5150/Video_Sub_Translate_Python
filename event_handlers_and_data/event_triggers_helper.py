from event_handlers_and_data.event_dispatchers import EventDispatchers


def trigger_success_fail(dispatcher: EventDispatchers, event_success, event_fail, func):
    """
	Just avoids boiler plate where it feels like it would get a little too verbose

    dispatcher : EventHandler
        The dispatcher instance to trigger events on.
    event_success : callable
        Function returning a StatusData object for success.
    event_fail : callable
        Function returning a StatusData object for failure, takes Exception | str.
    func : callable
        The function to execute safely.
    """
    try:
        result = func()
        dispatcher.trigger_event(event_success())
        return result
    except Exception as e:
        dispatcher.trigger_event(event_fail(e))
        return None