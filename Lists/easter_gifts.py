# Create a program that helps you plan the gifts for your friends and family. First, you are going to receive the gifts you plan on buying on a single line, separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
# •	"OutOfStock {gift}"
# o	Find the gifts with this name in your collection, if any, and change their values to "None".  
# •	"Required {gift} {index}"
# o	If the index is valid, replace the gift on the given index with the given gift. 
# •	"JustInCase {gift}"
# o	Replace the value of your last gift with this one. 
# In the end, print the gifts on a single line, except the ones with the value "None", separated by a single space in the following format:
# "{gift1} {gift2} {gift3} … {giftn}"


planned_gifts = input().split(" ")

while True:
    command = input()
    command_to_list = command.split(" ")
    if command == "No Money":
        break
    elif command_to_list[0] == "OutOfStock":
        for i in range(len(planned_gifts)):
            if command_to_list[1] == planned_gifts[i]:
                planned_gifts[i] = "None"
    elif command_to_list[0] == "Required":            
        position_to_integer = int(command_to_list[2])  
        if position_to_integer > len(planned_gifts):  # Making sure the position input is avlid and within the range of the current list
            continue
        for i in range(len(planned_gifts)):
            if i == position_to_integer:
                planned_gifts[i] = command_to_list[1]
    elif command_to_list[0] == "JustInCase":
        planned_gifts[-1] = command_to_list[1]

final_list = []
for gift in planned_gifts:
    if gift != "None":
        final_list.append(gift)

print(" ".join(final_list))
