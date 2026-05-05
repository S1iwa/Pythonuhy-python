import time
from functools import lru_cache

from lista7.zad4.make_generator import make_generator
from lista7.zad5.make_generator_mem import make_generator_mem



c = 0
def square(n):
    global c
    c += 1
    return n * n


#Rekurencja
# bez memo
c1 = 0
def fib(n):
    global c1
    c1 += 1
    return 1 if n <= 2 else fib(n-1) + fib(n-2)


# z memo
c2 = 0
@lru_cache(maxsize=None)
def fib2(n):
    global c2
    c2 += 1
    return 1 if n <= 2 else fib2(n-1) + fib2(n-2)


if __name__ == "__main__":

    gen1, cached_f = make_generator_mem(square)
    for _ in range(5):
        next(gen1)  # zapisuje w cache

    print(f"Wywołania: {c}")

    c = 0  # reset licznika

    gen2, cached_f = make_generator_mem(cached_f)
    for _ in range(5):
        next(gen2)  # pobiera z cache

    print(f"Wywołania: {c}")


    # Rekurencja
    #mem
    g1 = make_generator(fib)
    for _ in range(10):
        next(g1)

    #bez mem
    g2, _ = make_generator_mem(fib2)
    for _ in range(10):
        next(g2)

    print(f"bez memo: {c1}")
    print(f"z memo:   {c2}")
