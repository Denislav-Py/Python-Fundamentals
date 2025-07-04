# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-".
# If you receive a name that already exists in the phonebook, update its number.
# After filling out the phonebook, you will receive a number – N.
# Your program should be able to perform a search of contact by name and print its details in the format: "{name} -> {number}".
# In case the contact isn't found, print: "Contact {name} does not exist."

phone_book = {}
n = 0

while True:
    data = input()
    if data.isnumeric():
        n = int(data)
        break

    key, value = data.split("-")
    phone_book[key] = value


for _ in range(n):
    contact = input()
    if contact in phone_book.keys():
        print(f"{contact} -> {phone_book[contact]}")
    else:
        print(f"Contact {contact} does not exist.")
