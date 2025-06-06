# A palindrome is a number that reads the same backward as forward, such as 323 or 1001.
# Write a function that receives a list of positive integers, separated by comma and space ", ".
# The function should check if each integer is a palindrome - True or False. Print the result.

def is_palindrome(some_list: str) -> bool:
    return some_list == some_list[::-1]


number_as_list = input().split(", ")
for item in number_as_list:
    print(is_palindrome(item))
