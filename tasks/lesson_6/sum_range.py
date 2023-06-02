def sum_range(start: int, end: int):
    start, end = sorted([start, end])
    return sum(range(start, end+1))