# Write a function that receives two integer numbers. Calculate the factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.

def factorial_division(num: int) -> int:
    factorial = 1
    for number in range(1, num + 1):
        factorial *= number
    return factorial


first_number = int(input())
second_number = int(input())

print(f"{factorial_division(first_number) / factorial_division(second_number):.2f}")
