# Using comprehension, write a program that receives a text and removes all its vowels, case insensitive. 
# Print the new text string after removing the vowels. The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.

text_input = input()

vowels = ['a', 'o', 'u', 'e', 'i']

text_without_vowels = [letter for letter in text_input if letter.lower() not in vowels]

print("".join(text_without_vowels))
