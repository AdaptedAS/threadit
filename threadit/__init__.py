import threading
import warnings
from functools import wraps

_results = {}


def thredit_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        name = func.__name__
        result = func(*args, **kwargs)
        _results[name] = result

    return wrapper


class Threadit:
    def __init__(self, func, *args):
        self.name = func.__name__
        self.thread = threading.Thread(target=func, args=args)
        self.thread.start()

    def doing_working(self):
        return self.thread.is_alive()

    def get(self):
        self.thread.join()
        try:
            this_result = _results[self.name]
            del _results[self.name]
            return this_result
        except KeyError:
            warnings.warn(
                "Could not find result for Threadit object. Are you sure the function is decorated with @threadit_result?",
                SyntaxWarning
            )
