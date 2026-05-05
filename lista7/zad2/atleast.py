def atleast(n, pred, iterable):
    return sum(map(pred, iterable)) >= n