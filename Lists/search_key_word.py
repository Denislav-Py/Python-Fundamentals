# On the first line, you will receive a number n.
# On the second line, you will receive a word.
# On the following n lines, you will be given some strings. You should add them to a list and print them.
# After that, you should filter out only the strings that include the given word and print that list too.

number_of_inputs = int(input())

key_word = input()

full_list = []
filtered_list = []

for string in range(number_of_inputs):  
    current_string = input()
    full_list.append(current_string)    # Creating the full list

for string in full_list:                # Create new list only containing the key word
    if key_word in string:
        filtered_list.append(string)

print(f"{full_list} \n"
      f"{filtered_list}")
