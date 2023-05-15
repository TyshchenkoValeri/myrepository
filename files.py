import datetime


def log_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("results.txt", "a") as f:
            f.write(f"Function launched at {timestamp} with result {result}\n")
        return result
    return wrapper


@log_result
def sum_values(*args):
    result = sum(args)
    return result


sum_values(1, 2, 3, 4)