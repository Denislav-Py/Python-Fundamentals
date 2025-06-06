# Write a program that receives a sequence of numbers (integers) separated by a single space. It should print the min and max values of the given numbers and the sum of all the numbers in the list. Use min(), max() and sum().
# The output should be as follows:
# •	On the first line: "The minimum number is {minimum number}"
# •	On the second line: "The maximum number is {maximum number}"
# •	On the third line: "The sum number is: {sum of all numbers}"

def min_max_sum(list_of_numbers: list):
    minimum_number = min(numbers_as_digits)
    maximum_number = max(numbers_as_digits)
    total_sum = sum(numbers_as_digits)
    return f"The minimum number is {minimum_number}\n" \
           f"The maximum number is {maximum_number}\n" \
           f"The sum number is: {total_sum}"


numbers_as_strings = input().split()
numbers_as_digits = []
for item in numbers_as_strings:
    numbers_as_digits.append(int(item))

print(min_max_sum(numbers_as_digits))
