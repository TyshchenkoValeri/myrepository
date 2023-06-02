def is_prime(number):
    """
     Calculating is given number belong to prime numbers or not
    :param number: int
    :return: bool
    """
    if number < 2 or number > 1000:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
