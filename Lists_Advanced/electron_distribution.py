# You will receive a single integer - the number of electrons. Your task is to fill shells until there are no more electrons left. The rules for electron distribution are as follows:
# •	The maximum number of electrons in a shell can be 2n2, where n is the position of a shell (starting from 1). For example, the maximum number of electrons in the 3rd shield can be 2*32 = 18.
# •	You should start filling the shells from the first one at the first position.
# •	If the electrons are enough to fill the first shell, the left unoccupied electrons should fill the following shell and so on.
# In the end, print a list with the filled shells.

number_of_electrons = int(input())
shell = 0
filled_list = []

while number_of_electrons > 0:
    shell += 1

    max_electrons = 2 * shell ** 2
    if max_electrons <= number_of_electrons:
        filled_list.append(max_electrons)
        number_of_electrons -= max_electrons
    else:
        filled_list.append(number_of_electrons)
        break

print(filled_list)
