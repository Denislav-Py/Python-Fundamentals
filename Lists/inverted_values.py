# Write a program that receives a single string containing positive and negative numbers,
# separated by a single space. Print a list containing the opposite of each number.

string = input()

string_list = string.split(" ")

new_list = []

for i in string_list:
    current_number = int(i) * -1
    new_list.append(current_number)

print(new_list)
