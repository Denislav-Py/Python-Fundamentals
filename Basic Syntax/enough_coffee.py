# Your task is to define how much coffee you need to stay awake.
# Until you receive the command "END", you need to read commands on different lines.
# According to the commands, calculate the number of coffees you need to drink to stay awake during the daytime.
# The list of events can contain the following:
# •	You have homework to do ("coding").
# •	You have a dog or a cat that decided to wake you up too early ("dog" or "cat").
# •	You watch a movie ("movie").
# •	If other events are present, they will be represented by arbitrary strings. Just ignore them!
# Each event can be lowercase or uppercase:
# •	If it is lowercase, you need 1 coffee by an event.
# •	If it is uppercase, you need 2 coffees by an event.
# In the end, print the number of coffees you will need. If the count has exceeded 5, just print "You need extra sleep".

import string

total_coffees = 0

while True:
    command = input()
    if command == "END":
        print(f"{total_coffees}")
        break

    converted = command.lower()
    if converted != "coding" and converted != "dog" and converted != "cat" and converted != "movie":
        continue
    else:
        if command.islower():
            total_coffees += 1
        elif command .isupper():
            total_coffees += 2

    if total_coffees > 5:
        print(f"You need extra sleep")
        break
