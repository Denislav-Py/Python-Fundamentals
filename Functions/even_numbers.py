# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a list of only the even numbers. Use filter().

def even_numbers(n):
    return n % 2 == 0


list_of_numbers = input().split()

numbers_list = []

for item in list_of_numbers:
    numbers_list.append(int(item))

final_list = filter(even_numbers, numbers_list)

print(list(final_list))
