# You will receive two lines of input:
# •	a list of employees' happiness as a string of numbers separated by a single space
# •	a happiness improvement factor (single number).
# Your task is to find out if the employees are generally happy in their office.
# First, multiply each employee's happiness by the factor.
# Then, print one of the following lines:
# •	If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
# •	Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"

employees_happiness = list(map(int, input().split()))
factor = int(input())

multiplied = [num * factor for num in employees_happiness]
average_happiness = sum(multiplied) / len(multiplied)

happy_counter = sum(1 for num in multiplied if num >= average_happiness)
total_people = len(multiplied)

if happy_counter >= (len(multiplied) // 2):
    print(f"Score: {happy_counter}/{total_people}. Employees are happy!")
else:
    print(f"Score: {happy_counter}/{total_people}. Employees are not happy!")
