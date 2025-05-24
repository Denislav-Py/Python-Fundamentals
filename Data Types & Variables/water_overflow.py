# You have a water tank with a capacity of 255 liters.
# On the first line, you will receive n – the number of lines, which will follow. On the following n lines,
# you will receive liters of water (integers), which you should pour into your tank. If the capacity is not enough,
# print "Insufficient capacity!" and continue reading the next line. On the last line, print the liters in the tank.

total_capacity = 255
number_of_pours = int(input())

capacity_left = 255

for _ in range(number_of_pours):
    liters = int(input())

    if capacity_left < liters:
        print("Insufficient capacity!")
        continue
    else:
        capacity_left -= liters

print(f"{total_capacity - capacity_left}") # Total liters of water poured in
