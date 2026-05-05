def make_generator(f):
    def generator():
        n = 1
        while True:
            # yield zamraża stan funkcji i zwraca wartość f(n)
            yield f(n)
            n += 1
    return generator()