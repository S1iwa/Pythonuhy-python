from functools import lru_cache
from lista7.zad4.make_generator import make_generator


def make_generator_mem(f, maxsize=None):
    # tworzenie cache jeżeli funkcja nie jest już zmemoizowana
    cached_f = f if hasattr(f, 'cache_info') else lru_cache(maxsize=maxsize)(f)

    # użycie starej funkcji + zwrócenie cache, aby dało się go użyć dla innego generatora
    return make_generator(cached_f), cached_f