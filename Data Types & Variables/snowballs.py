# You will receive N – an integer, the number of snowballs being made by Tony and Andi.
# On the following lines, you will receive 3 inputs for each snowball:
# •	The weight of the snowball (integer).
# •	The time needed for the snowball to get to its target (integer).
# •	The quality of the snowball (integer).
# For each snowball, you must calculate its value by the following formula:
# (snowball_weight / snowball_time) ** snowball_quality
# In the end, you must print the highest calculated value of a snowball.
import sys

total_number_of_snowballs = int(input())

highest_value = -sys.maxsize
weight = 0
velocity = 0
quality = 0

for sb in range(total_number_of_snowballs):
    snowball_weight = int(input())
    snowball_velocity = int(input())
    snowball_quality = int(input())

    value = (snowball_weight // snowball_velocity) ** snowball_quality
    if value > highest_value:
        highest_value = value
        weight = snowball_weight
        velocity = snowball_velocity
        quality = snowball_quality

print(f"{weight} : {velocity} = {highest_value} ({quality})")
