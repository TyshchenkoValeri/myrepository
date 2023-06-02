# 1.
names = ["john", "marta", "james", "amanda", "marianna"]
capitalized_names = [name.capitalize() for name in names]

print(capitalized_names)

# 2.
friends = ["John", "Marta", "James", "Amanda", "Marianna"]
name_header = "NAME".center(10, "*")

print(name_header)
for name in friends:
    formatted_name = f"{name:>10}"
    print(formatted_name)

# 3.
variables = ["FirstItem", "FriendsList", "MyTuple"]

snake_case_vars = []
for var in variables:
    snake_case_var = ""
    for i, c in enumerate(var):
        if c.isupper() and i != 0:
            snake_case_var += "_"
        snake_case_var += c.lower()
    snake_case_vars.append(snake_case_var)

print(snake_case_vars)

# 4.
# Створюємо словник мов програмування та розробників
programming_languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "JavaScript": "Brendan Eich",
    "C++": "Bjarne Stroustrup"
}

# Виводимо повідомлення про кожен елемент словника
for language, developer in programming_languages.items():
    print(f"My favorite programming language is {language}. It was created by {developer}.")

# Видаляємо одну пару зі словника
del programming_languages["JavaScript"]

# Виводимо оновлений словник на екран
print(programming_languages)

# 5.
# Створюємо словник англо-німецьких перекладів
e2g = {
    "stork": "storch",
    "hawk": "falke",
    "woodpecker": "specht",
    "owl": "eule"
}

# Виводимо словник на екран
print(e2g)

# Виводимо німецький варіант слова "owl"
print("German version of the word owl:", e2g["owl"])

# Додаємо ще два слова та їх переклади
e2g["pigeon"] = "taube"
e2g["swan"] = "schwan"

# Виводимо словник на екран
print("Updated dictionary:", e2g)

# Виводимо ключі словника у вигляді списку
print("Dictionary keys:", list(e2g.keys()))

# Виводимо значення словника у вигляді списку
print("Dictionary meaning:", list(e2g.values()))

# 6.
# Створення багаторівневого словника subjects
subjects = {
    'science': {
        'physics': ['nuclear physics', 'optics', 'thermodynamics'],
        'computer science': {},
        'biology': {}
    },
    'humanities': {},
    'public': {}
}

# Виведення ключів subjects['science'] та значення subjects['science']['physics']
print(subjects['science'].keys())  # виведе dict_keys(['physics', 'computer science', 'biology'])
print(subjects['science']['physics'])  # виведе ['nuclear physics', 'optics', 'thermodynamics']

# 7.
square_dict = {}
for num in range(1, 16):
    square_dict[num] = num ** 2

print(square_dict)