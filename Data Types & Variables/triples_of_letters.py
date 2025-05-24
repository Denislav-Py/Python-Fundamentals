# Write a program to read an integer N and print all triples of the first N small Latin letters, ordered alphabetically

number_of_letters = int(input())

for j in range(97, 97 + number_of_letters):
    for k in range(97, 97 + number_of_letters):
        for l in range(97, 97 + number_of_letters):
            print(f"{chr(j)}{chr(k)}{chr(l)}")
