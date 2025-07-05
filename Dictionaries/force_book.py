# The force users struggle to remember which side is the different force users from because they switch them too often. 
# So you are tasked to create a web application to manage their profiles. You should store information for every unique force user registered in the application.
# You will receive several input lines in one of the following formats:
# "{force_side} | {force_user}"
# "{force_user} -> {force_side}"
# The "force_user" and "force_side" are strings, containing any character. 
# If you receive "force_side | force_user":
# •	If there is no such force user and no such force side -> create a new force side and add the force user to the corresponding side.
# •	Only if there is no such force user in any force side -> add the force user to the corresponding side. 
# •	If there is such force user already -> skip the command and continue to the next operation.
# If you receive a "force_user -> force_side":
# •	If there is such force user already -> change their side. 
# •	If there is no such force user in any force side -> add the force user to the corresponding force side.
# •	If there is no such force user and no such force side -> create new force side and add the force user to the corresponding side.
# •	Then you should print on the console: "{force_user} joins the {force_side} side!".
# You should end your program when you receive the command "Lumpawaroo". At that point, you should print each force side. For each side, print the force users.
# In case there are no forced users on a side, you shouldn't print the side information.

force_dictionary = {}

while True:
    data = input()
    if data == "Lumpawaroo":
        break

    if "|" in data:
        force_side, force_user = data.split(" | ")
        force_user_found = False
        for force_users_list in force_dictionary.values():
            if force_user in force_users_list:
                force_user_found = True
                break
        if not force_user_found:
            if force_side not in force_dictionary.keys():
                force_dictionary[force_side] = []
            force_dictionary[force_side].append(force_user)
    elif "->" in data:
        force_user, force_side = data.split(" -> ")
        for force_users_list in force_dictionary.values():
            if force_user in force_users_list:
                force_users_list.remove(force_user)
                break
        if force_side not in force_dictionary.keys():
            force_dictionary[force_side] = []
        force_dictionary[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")


for force, user in force_dictionary.items():
    if len(force_dictionary[force]) > 0:
        print(f"Side: {force}, Members: {len(force_dictionary[force])}")
        for usr in force_dictionary[force]:
            print(f"! {usr}")
