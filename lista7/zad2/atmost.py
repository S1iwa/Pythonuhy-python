def atmost(n, pred, iterable):
    return sum(map(pred, iterable)) <= n