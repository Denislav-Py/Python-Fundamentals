# You will be given a string representing the version of your software in the format: "{n1}.{n2}.{n3}".
# Your task is to print the next version. For example, if the current version is "1.3.4", the next version will be "1.3.5".
# The only rule is that the numbers cannot be greater than 9.
# If it happens, set the current number to 0 and increase the previous number. For more clarification, see the examples below

current_version = int("".join(input().split(".")))
next_version = current_version + 1

print(f"{'.'.join(str(next_version))}")
