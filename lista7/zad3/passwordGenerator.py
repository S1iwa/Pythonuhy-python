import random
import string

class PasswordGenerator:
    def __init__(self, length, charset=None, count=10):
        self.length = length
        # Jeśli charset niepodany to używamt liter i cyfr
        self.charset = charset if charset else string.ascii_letters + string.digits
        self.count = count
        self.current = 0

    # Metoda wymagana przez protokół iteratora
    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.count:
            raise StopIteration

        password = "".join(random.choices(self.charset, k=self.length))
        self.current += 1
        return password