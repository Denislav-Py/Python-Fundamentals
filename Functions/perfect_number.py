# A perfect number is a positive integer that is equal to the sum of its proper positive divisors. That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
# Write a function that receives an integer number and returns one of the following messages:
# •	"We have a perfect number!" - if the number is perfect.
# •	"It's not so perfect." - if the number is NOT perfect.
# Print the result on the console.

def perfect_number(num: int) -> str:
    divisor_sum = 0
    for number in range(1, num):
        if num % number == 0:
            divisor_sum += number

    if divisor_sum == num:
        return "We have a perfect number!"
    return "It's not so perfect."


initial_number = int(input())
print(perfect_number(initial_number))
