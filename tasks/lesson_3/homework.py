# test_directory.
word = input("Enter the word: ").lower()
is_polin = word[::-1]
print("+" if is_polin == word else "-")


# 2.
text = input("Enter the text: ")
word = input("Enter the word: ")

print("yes" if word in text else "no")


# 3.
some_string = input("Enter the text: ").lower()

if some_string.startswith("abc"):
    some_string = some_string.replace("abc", "www")
    print(some_string)
else:
    some_string += "zzz"
    print(some_string)


# 4.
check_email = input("Enter the e-mail: ")
print("Yes" if "@" and "." in check_email else "No")


# 5.
some_text = input("Enter the text: ")
some_text = some_text.split()

if len(some_text) < 3:
    print("The number of elements is less than 3. Number of elements in the current list is", len(some_text))
else:
    print(some_text[-3:])


