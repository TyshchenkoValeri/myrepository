# 1.
def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    assert discriminant >= 0, "The equation has complex roots."
    x1 = (-b + discriminant**0.5) / (2*a)
    x2 = (-b - discriminant**0.5) / (2*a)
    return x1, x2


try:
    a = int(input("Enter the coefficient a: "))
    b = int(input("Enter the coefficient b: "))
    c = int(input("Enter the coefficient c: "))
    roots = solve_quadratic_equation(a, b, c)
    print(f"The roots of the equation: {roots}")
except (ValueError, AssertionError) as e:
    print("Incorrect input or equation has complex roots:", e)

# 2.
def calculate():
    formula = input("Enter the formula: ")
    parts = formula.split()
    if len(parts) != 3:
        raise ValueError("The formula should consist of three elements")
    try:
        num1 = float(parts[0])
        num2 = float(parts[2])
    except ValueError:
        raise ValueError("The first and third elements must be numbers")
    if parts[1] not in ['+', '-']:
        raise ValueError("The second element must be + or -")
    if parts[1] == '+':
        result = num1 + num2
    else:
        result = num1 - num2
    print(f"Result: {result}")


while True:
    try:
        calculate()
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nThank you for using the calculator!")
        break