import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function execution time {func.__name__}: {end_time - start_time: .2f} seconds")
        return result
    return wrapper


@timer
def some_function():
    pass


print(some_function())