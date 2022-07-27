import threading


SECRET_KEY = "C2D6uJ0rpqaQJ1RIZJH8x21BMX7Pq14QWcSoqoTN"


def thread_decorator(func):
    """Decorator turns function into thread.
    Requires func.start() to activate function.
    """
    def wrapper(*args, **kwargs) -> threading.Thread:
        thread = threading.Thread(target=func, args=(*args, ))
        return thread
    return wrapper
