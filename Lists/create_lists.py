# On the first line, you will receive a single number n.
# On the following n lines, you will receive names of courses. You should create a list of courses and print it.

number_of_courses = int(input())

courses = []

for course in range(number_of_courses):
    current_course = input()

    courses.append(current_course)

print(courses)
