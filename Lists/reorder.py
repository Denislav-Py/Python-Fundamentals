# You are at the zoo, and the meerkats look strange. 
# You will receive 3 strings on separate lines, representing the tail, the body, and the head of an animal in that order. 
# Your task is to re-arrange the elements in a list so that the animal looks normal again:
# •	On the first position is the head;
# •	On the second position is the body;
# •	On the last one is the tail.

number_of_inputs = 3

string_list = []

for string in range(number_of_inputs):
    current_input = input()
    string_list.append(current_input)

string_list[0], string_list[2] = string_list[2], string_list[0]

print(string_list)
