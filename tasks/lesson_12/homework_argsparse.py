import argparse
import math


def calculate_quadratic_equation(a, b, c):
    if a == 0:
        print("Parameter 'a' cannot be zero.")
        return

    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        print("The equation has two roots:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif discriminant == 0:
        x = -b / (2*a)
        print("The equation has one root:")
        print(f"x = {x}")
    else:
        print("The equation has no real roots.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Program for calculating a quadratic equation.")
    parser.add_argument("-a", type=float, default=0, help="parameter 'a' of the quadratic equation")
    parser.add_argument("-b", type=float, required=True,
                        help="parameter 'b' of the quadratic equation")
    parser.add_argument("-c", type=float, required=True, help="parameter 'c' of the quadratic equation")

    args = parser.parse_args()

    calculate_quadratic_equation(args.a, args.b, args.c)
