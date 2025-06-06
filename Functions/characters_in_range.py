# Write a function that receives two characters and returns a single string with all the characters in between them 
# (according to the ASCII code), separated by a single space. Print the result on the console.

def characters_in_range():
    starting_letters = []
    for _ in range(2):
        current_item = input()
        starting_letters.append(current_item)

    for item in range(ord(starting_letters[0]) + 1, ord(starting_letters[1])):
        print(chr(item), end=" ")


characters_in_range()
