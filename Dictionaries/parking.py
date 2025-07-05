# SoftUni just got a new fancy parking lot. It even has online parking validation, except the online service doesn't work. 
# It can only receive users' data, but it doesn't know what to do with it. Good thing you're on the dev team and know how to fix it, right? 
# 
# Write a program, which validates a parking place - users can register to enter the park and unregister to leave. 
# 
# The program receives 2 types of commands: 
# 
# "register {username} {license_plate_number}": 
# 
# The system only supports one car per user at the moment, so if a user tries to register another license plate using the same username, the system should print: 
# "ERROR: already registered with plate number {license_plate_number}" 
# 
# If the check above passes successfully, the user should be registered, so the system should print: 
#  "{username} registered {license_plate_number} successfully" 
# 
# "unregister {username}": 
# 
# If the user is not present in the database, the system should print: 
# "ERROR: user {username} not found" 
# 
# If the check above passes successfully, the system should print: 
# "{username} unregistered successfully" 
# 
# After you execute all of the commands, print all the currently registered users and their license plates in the format:  
# 
# "{username} => {license_plate_number}" 

number_of_commands = int(input())

users = {}

for i in range(0, number_of_commands):
    command = input().split()
    if command[0] == "register":
        user = command[1]
        license_plate = command[2]
        if user in users.keys():
            print(f"ERROR: already registered with plate number {users[user]}")
        else:
            users[user] = license_plate
            print(f"{user} registered {license_plate} successfully")
    elif command[0] == "unregister":
        user = command[1]
        if user not in users.keys():
            print(f"ERROR: user {user} not found")
        else:
            print(f"{user} unregistered successfully")
            del users[user]

for person, plate in users.items():
    print(f"{person} => {plate}")
