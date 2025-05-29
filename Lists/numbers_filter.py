# On the first line, you will receive a single number n. On the following n lines, you will receive integers.
# After that, you will be given one of the following commands:
# •	even
# •	odd
# •	negative
# •	positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.

number_of_inputs = int(input())

full_list = []
filtered_list = []

for num in range(number_of_inputs):    # Adding all numbers into one list
    current_number = int(input())
    full_list.append(current_number)

command = input()

if command == "even":                  # Comparing comand and condition to fill in the filtered list
    for number in full_list:
        if number % 2 == 0:
            filtered_list.append(number)
elif command == "odd":
    for number in full_list:
        if number % 2 != 0:
            filtered_list.append(number)
elif command == "negative":
    for number in full_list:
        if number < 0:
            filtered_list.append(number)
elif command == "positive":
    for number in full_list:
        if number >= 0:
            filtered_list.append(number)

print(filtered_list)
