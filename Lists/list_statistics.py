# On the first line, you will receive a number n. On the following n lines, you will receive integers. You should create and print two lists:
# •	One with all the positive (including 0) numbers
# •	One with all the negative numbers
# Finally, print the following message:
# "Count of positives: {count_positives}
# Sum of negatives: {sum_of_negatives}"

number_of_inputs = int(input())

positive_numbers = []
negative_numbers = []

for num in range(number_of_inputs):
    current_number = int(input())

    if current_number < 0:
        negative_numbers.append(current_number)
    else:
        positive_numbers.append(current_number)

print(f"{positive_numbers} \n"
      f"{negative_numbers}")

print(f"Count of positives: {len(positive_numbers)} \n"
      f"Sum of negatives: {sum(negative_numbers)}")
