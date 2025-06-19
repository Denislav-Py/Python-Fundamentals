# You will receive a sequence of integers, separated by spaces - the distances to the pokemon. Then you will begin receiving integers, which will correspond to indexes in that sequence.
# When you receive an index, you must remove the element at that index from the sequence (as if you've captured the pokemon).
# •	You must increase the value of all elements in the sequence that are less or equal to the removed element with the value of the removed element.
# •	You must decrease the value of all elements in the sequence that are greater than the removed element with the value of the removed element.
# If the given index is less than 0, remove the first element of the sequence, and copy the last element to its place.
# If the given index is greater than the last index of the sequence, remove the last element from the sequence, and copy the first element to its place.
# The increasing and decreasing elements should also be done in these cases. The element whose value you should use is the removed element.
# The program ends when the sequence has no elements

pokemons = list(map(int, input().split()))
test_list = []
total_sum = 0

while pokemons:
    index = int(input())

    if index < 0:
        index = 0
        test_list.append(pokemons[index])
        pokemons.pop(index)
        pokemons.insert(index, pokemons[-1])
        for i in range(len(pokemons)):
            if pokemons[i] <= test_list[-1]:
                pokemons[i] += test_list[-1]
            else:
                pokemons[i] -= test_list[-1]
        total_sum += test_list[-1]
    elif index > len(pokemons) - 1:
        index = len(pokemons) - 1
        test_list.append(pokemons[index])
        pokemons.pop(index)
        pokemons.insert(index, pokemons[0])
        for i in range(len(pokemons)):
            if pokemons[i] <= test_list[-1]:
                pokemons[i] += test_list[-1]
            else:
                pokemons[i] -= test_list[-1]
        total_sum += test_list[-1]
    else:
        test_list.append(pokemons[index])
        pokemons.pop(index)
        for i in range(len(pokemons)):
            if pokemons[i] <= test_list[-1]:
                pokemons[i] += test_list[-1]
            else:
                pokemons[i] -= test_list[-1]
        total_sum += test_list[-1]

print(total_sum)
