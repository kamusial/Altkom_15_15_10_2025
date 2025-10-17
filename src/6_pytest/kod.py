def fizzbuss(i):
    if i % 15 == 0:
        return 'fizzbuzz'
    elif i % 3 == 0:
        return 'fizz'
    elif i % 5 == 0:
        return 'buzz'
    return i