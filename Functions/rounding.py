# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list.
# Use round().

initial_list = input().split()

numbers_list = []

for item in initial_list:
    numbers_list.append(round(float(item)))

print(numbers_list)
