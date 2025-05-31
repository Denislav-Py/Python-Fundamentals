# Create a program that calculates the water needed to put out a "fire cell", based on the given information about its "fire level" and how much it gets affected by water.
# First, you will be given the level of fire inside the cell with the integer value of the cell, which represents the needed water to put out the fire.  They will be given in the following format:
# "{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}# … {typeOfFire} = {valueOfCell}"
# Afterward, you will receive the amount of water you have for putting out the fires. 
# There is a range of fire for each fire type, and if a cell's value is below or exceeds it, it is invalid, and you do not need to put it out.
# Type of Fire	Range
# High	81 - 125
# Medium	51 – 80
# Low	1 - 50
# If a cell is valid, you should put it out by reducing the water with its value. 
# Putting out fire also takes effort, and you need to calculate it. Its value is equal to 25% of the cell's value. 
# In the end, you will have to print the total effort. Keep putting out cells until you run out of water. 
# Skip it and try the next one if you do not have enough water to put out a given cell. In the end, print the cells you have put out in the following format:
# "Cells:
#  - {cell1}
#  - {cell2}
#  …
#  - {cellN}"
# "Effort: {effort}"
# The effort should be formatted to the second decimal place.
# In the end, print the total fire you have put out from all the cells in the following format:
# "Total Fire: {total_fire}"

level_of_fire = input().split("#")
amount_of_water = int(input())
effort = 0.0

clean_list = []
cells_list = []

for i in range(len(level_of_fire)):
    level, cell = level_of_fire[i].split(" = ")
    cell = int(cell)

    if amount_of_water < cell:
        continue
    elif level == "High" and 81 <= cell <= 125:
        amount_of_water -= cell
        effort += cell * 0.25
        cells_list.append(cell)
    elif level == "Medium" and 51 <= cell <= 80:
        amount_of_water -= cell
        effort += cell * 0.25
        cells_list.append(cell)
    elif level == "Low" and 1 <= cell <= 50:
        amount_of_water -= cell
        effort += cell * 0.25
        cells_list.append(cell)


print("Cells:")
for fire in cells_list:
    print(f" - {fire}")

print(f"Effort: {effort:.2f} \nTotal Fire: {sum(cells_list)}")
