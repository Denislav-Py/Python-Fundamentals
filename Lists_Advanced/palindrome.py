# On the first line, you will receive words separated by a single space. 
# On the second line, you will receive a palindrome. 
# First, you should print a list containing all the found palindromes in the sequence. 
# Then, you should print the number of occurrences of the given palindrome in the format: 
# "Found palindrome {number} times".


first_line = input().split()
given_palindrome = input()

palindrome_list = [item for item in first_line if item == item[::-1]]

counter = 0

for item in palindrome_list:
    if item == given_palindrome:
        counter += 1

print(palindrome_list)
print(f"Found palindrome {counter} times")
