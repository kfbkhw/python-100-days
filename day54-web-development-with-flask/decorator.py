import time


def speed_calc_decorator(function):
    def wrapper():
        start = time.time()
        function()
        end = time.time()
        speed = end - start
        return f"{function.__name__} run speed: {speed}s"

    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


print(fast_function())
print(slow_function())
