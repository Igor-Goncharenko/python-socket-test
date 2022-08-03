import threading


def thread_decorator(func):
    """Decorator turns function into thread.
    Requires func.start() to activate function.
    """
    def wrapper(*args, **kwargs) -> threading.Thread:
        thread = threading.Thread(target=func, args=(*args, ))
        return thread
    return wrapper
