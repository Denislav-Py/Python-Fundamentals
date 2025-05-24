# Calculate how many courses will be needed to elevate N persons by using an elevator with a capacity of P persons.
# The input holds two lines: the number of people N and the capacity P of the elevator.

from math import ceil

number_of_people = int(input())
capacity = int(input())

total_courses = ceil(number_of_people / capacity) # Using "ceil" since there cannot be half courses.
print(f"{total_courses}")
