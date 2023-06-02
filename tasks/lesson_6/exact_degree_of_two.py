def exact_degree_of_two(number: int):
    while number >= 2:
        number = number / 2
    if 1 == number:
        print("YES")
    else:
        print("NO")