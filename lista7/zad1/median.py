def median(numbers):
    s = sorted(numbers)
    n = len(numbers)
    return s[n//2] if n % 2 != 0 else (s[n//2 - 1] + s[n//2]) / 2