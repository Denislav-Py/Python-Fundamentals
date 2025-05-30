# A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half. Then the cards in the two halves are perfectly interleaved, such that the original bottom card is still on the bottom and the original top card is still on top.
# For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six']
# Write a program that receives a single string (cards separated by space) and on the second line receives a count of faro shuffles that should be made. Print the state of the deck after the shuffle.
# Note: The length of the deck of cards will always be an even number.

string = input().split(" ")
number_of_shuffles = int(input())

for _ in range(number_of_shuffles):
    half_split = len(string) // 2  # Split the string in half
    first_half = string[0:half_split]  # Fill in first half with current string data
    second_half = string[half_split::]  # Fill in second half with current string data
    current_shuffle = []  # Empty list to be filled with each separate shuffle

    for char in range(half_split):
        current_shuffle.append(first_half[char])
        current_shuffle.append(second_half[char])

    string = current_shuffle  # Replace the original string with data from current shuffle

print(string)
