def mnozenie(a, b):
    if isinstance(a, str) or isinstance(b, str):
        return a * b
    return round(a * b, 5)


