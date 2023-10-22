def add(*args):
    result = 0
    for num in args:
        result += num
    return result


print(add(4, 5, 9, 10))


def calculate(n, **kwargs):
    n += kwargs["add"]
    n -= kwargs["subtract"]
    n *= kwargs["multiply"]
    n /= kwargs["divide"]
    return n


print(calculate(10, add=0, subtract=5, multiply=6, divide=3))
