# Write a program that receives a sequence of numbers (a string containing integers separated by ", ") 
# and prints the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
# Examples:
# •	The numbers 2, 8, 4, and 10 fall into the group of 10's.
# •	The numbers 13, 19, 14, and 15 fall into the group of 20's.

list_of_numbers = list(map(int, input().split(", ")))
threshold = 10
current_list = []
while list_of_numbers:
    for num in list_of_numbers:
        if num <= threshold:
            current_list.append(num)
    for num in current_list:
        if num in list_of_numbers:
            list_of_numbers.remove(num)

    print(f" Group of {threshold}'s: {current_list}")
    threshold += 10
    current_list.clear()
