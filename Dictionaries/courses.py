# Write a program that keeps the information about courses. Each course has a name and registered students. 
# 
# You will be receiving a course name and a student name until you receive the command "end".  
# 
# You should register each user into the corresponding course. If the given course does not exist, add it.  
# 
# When you receive the command "end", print the courses with their names and total registered users. For each course, print the registered users.

courses = {}

while True:
    data = input()
    if data == "end":
        break

    course, student = data.split(" : ")
    if course not in courses.keys():
        courses[course] = []
        courses[course].append(student)
    else:
        courses[course].append(student)

for topic in courses.keys():
    print(f"{topic}: {len(courses[topic])}")
    for person in courses[topic]:
        print(f"-- {person}")
