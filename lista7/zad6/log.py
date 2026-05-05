import logging
import time
from functools import wraps

#config do wyświetlania logów w konsoli
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log(level=logging.INFO):
    def decorator(obj):

        # Jeśli to funkcja
        if callable(obj) and not isinstance(obj, type):
            @wraps(obj)
            def wrapper(*args, **kwargs):
                start_time = time.time()
                logging.log(level, f"Wywołanie funkcji: {obj.__name__}")
                logging.log(level, f"Argumenty: args={args}, kwargs={kwargs}")

                result = obj(*args, **kwargs)

                end_time = time.time()
                duration = end_time - start_time

                logging.log(level, f"Zwrócona wartość: {result}")
                logging.log(level, f"Czas wykonania: {duration:.6f}s")

                return result

            return wrapper

        # Jeśli to klasa
        elif isinstance(obj, type):
            original_init = obj.__init__

            def __init__(self, *args, **kwargs):
                logging.log(level, f"Tworzenie instancji klasy: {obj.__name__}")
                logging.log(level, f"Argumenty: args={args}, kwargs={kwargs}")
                original_init(self, *args, **kwargs)

            obj.__init__ = __init__
            return obj

        return obj

    return decorator