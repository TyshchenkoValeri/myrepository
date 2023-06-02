import json

with open('manager_sales.json') as f:
    data = json.load(f)


# Створюємо словник для зберігання сум продажів для кожного менеджера
sales = {}

# Проходимо по кожному елементу списку і розраховуємо загальну суму продажів для кожного менеджера
for item in data:
    manager = item['manager']['first_name'] + ' ' + item['manager']['last_name']
    sales[manager] = 0
    for car in item['cars']:
        sales[manager] += car['price']

# Знаходимо менеджера з найбільшою загальною сумою продажів
best_manager = max(sales, key=sales.get)

# Виводимо відповідь у форматі, зазначеному у завданні
print(best_manager + ' ' + str(sales[best_manager]))


