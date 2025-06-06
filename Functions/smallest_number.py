# Write a function that receives three integer numbers and returns the smallest.
# Print the result on the console. Use an appropriate name for the function.
import sys


def smallest_number():
    min_number = []

    for item in range(3):
        current_number = int(input())

        min_number.append(current_number)

    return min(min_number)


print(smallest_number())
