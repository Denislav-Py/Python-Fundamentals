# Create a program that receives the n number of messages sent. On the following n lines, it will receive integer numbers. 
# For each number, the program should print a different message:
# •	If the number is 88 - "Hello"
# •	If the number is 86 - "How are you?"
# •	If the number is not 88 nor 86, and it is below 88 - "GREAT!"
# •	If the number is over 88 - "Bye."

number = int(input())

for _ in range(number):
    code = int(input())

    if code == 88:
        print("Hello")
    elif code == 86:
        print("How are you?")
    elif code != 88 and code != 86 and code < 88:
        print("GREAT!")
    elif code > 88:
        print("Bye.")
