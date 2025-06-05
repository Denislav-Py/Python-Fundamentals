# Write a program that receives a sequence of numbers, separated by a single space
# and prints their absolute value as a list. Use abs()

sequence = input().split()

absolute_value = []

for item in sequence:
    absolute_value.append(abs(float(item)))

print(absolute_value)
