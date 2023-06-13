# test_directory.
temp = int(input("Enter the temperature ib Celsius: "))
temp_far = (temp + 32) * 5/9
temp_kel = temp + 273.16
print("The temperature in Fahrenheit: ", temp_far)
print("The temperature in Kelvin: ", temp_kel)

# 2.
V1 = int(input("Enter the liters for V1: "))
T1 = int(input("Enter the temperature for T1: "))
V2 = int(input("Enter the liters for V2: "))
T2 = int(input("Enter the temperature for T2: "))

if V1 and V2 >= 0:
    result = (V1 * T1 + V2 * T2) / (V1 + V2)
    print("The volume and temperature of the resulting mixture is:", result)
else:
    print("You can't enter a negative value of liters! Try again")

# 3.
option = int(input("Choose the operation: test_directory - UAH --> USD, 2 - USD --> UAH, 3 - UAH --> EUR, 4 - EUR --> UAH): "))
rate_usd = int(input("Enter the rate USD to UAH: "))
rate_eur = int(input("Enter the rate EUR to UAH: "))

if option == 1:
    uah = int(input("Enter the amount in UAH: "))
    if uah <= 0:
        print("Incorrect amount")
    elif rate_usd <= 0 or rate_eur <= 0:
        print("Incorrect rate")
    else:
        usd = uah / rate_usd
        print("The sum in USD is: ", usd)
elif option == 2:
    usd = int(input("Enter the amount in USD: "))
    if usd <= 0:
        print("Incorrect amount")
    elif rate_usd <= 0 or rate_eur <= 0:
        print("Incorrect rate")
    else:
        uah = usd * rate_usd
        print("The sum in UAH is: ", uah)
elif option == 3:
    uah = int(input("Enter the amount in UAH: "))
    if uah <= 0:
        print("Incorrect amount")
    elif rate_usd <= 0 or rate_eur <= 0:
        print("Incorrect rate")
    else:
        eur = uah / rate_eur
        print("The sum in EUR is: ", eur)
elif option == 4:
    eur = int(input("Enter the amount in EUR: "))
    if eur <= 0:
        print("Incorrect amount")
    elif rate_usd <= 0 or rate_eur <= 0:
        print("Incorrect rate")
    else:
        uah = eur * rate_eur
        print("The sum in UAH is: ", uah)
else:
    print("Oops! It is an invalid operation! Try again.")

# 4.
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
act = input("Enter the action (+, -, *, /): ")

if act == "+":
    print(num_1 + num_2)
elif act == "-":
    print(num_1 - num_2)
elif act == "*":
    print(num_1 * num_2)
elif act == "/":
    if num_2 != 0:
        print(num_1 / num_2)
    else:
        print("You can't divide by zero! Try again.")
