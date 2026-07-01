class EventBus:
    _listeners = {}

    @classmethod
    def subscribe(cls, event_type: str, listener):
        if event_type not in cls._listeners:
            cls._listeners[event_type] = []
        cls._listeners[event_type].append(listener)

    @classmethod
    def emit(cls, event_type: str, data=None):
        if event_type in cls._listeners:
            for listener in cls._listeners[event_type]:
                listener(data)
