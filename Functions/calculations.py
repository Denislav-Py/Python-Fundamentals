# Create a function that receives three parameters, calculates a result depending on the given operator, and returns it. 
# Print the result of the function.
# The input comes as three parameters – an operator as a string and two integer numbers. 
# The operator can be one of the following:  "multiply", "divide", "add", and "subtract".


def calculator_function(operator, a, b):
    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        result = int(a / b)
    elif operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b
    return result


operator_ = input()
first_number = int(input())
second_number = int(input())

print(calculator_function(operator_, first_number, second_number))
