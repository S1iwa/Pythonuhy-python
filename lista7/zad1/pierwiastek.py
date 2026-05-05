def pierwiastek(x, epsilon = 0.1, y = 1.0):
    return y if abs(y**2 - x) < epsilon else pierwiastek(x, epsilon, ((y + x) / y) / 2)