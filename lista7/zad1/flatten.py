def flatten(lst):
    return sum([flatten(x) if isinstance(x, (list, tuple)) else [x] for x in lst], [])