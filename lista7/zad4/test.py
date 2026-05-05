from make_generator import make_generator


def fibonacci_n(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    print("Funkcja f samodzielnie zaimplementowana")
    fib_gen = make_generator(fibonacci_n)
    print("Fibonacci:", [next(fib_gen) for _ in range(5)])

    print("Funkcje lambdy")
    arytm = make_generator(lambda n: 5 + (n - 1))
    pow3 = make_generator(lambda n: n ** 3)

    print("Ciąg arytmetyczny:", [next(arytm) for _ in range(4)])
    print("Ciąg potęgowy:", [next(pow3) for _ in range(4)])