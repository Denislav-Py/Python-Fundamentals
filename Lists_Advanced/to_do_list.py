# You will be receiving to-do notes until you get the command "End". The notes will be in the format: "{importance}-{note}".
# Return a list containing all to-do notes sorted by importance in ascending order.
# The importance value will always be an integer between 1 and 10 (inclusive)


final_list = [0] * 10

while True:
    current_note = input()

    if current_note == "End":
        break

    importance, action = current_note.split("-")
    index = int(importance) - 1

    final_list.pop(index)
    final_list.insert(index, action)


result = [item for item in final_list if item != 0]
print(result)
