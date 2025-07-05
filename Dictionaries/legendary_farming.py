# You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough.
# However, it's a tedious process, and it requires quite a bit of farming. The possible items are:
# "Shadowmourne" - requires 250 Shards
# "Valanyr" - requires 250 Fragments
# "Dragonwrath" - requires 250 Motes
# "Shards", "Fragments", and "Motes" are the key materials 	(case-insensitive), and everything else is junk.
# You will be given lines of input in the format:
# "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# Keep track of the key materials - the first one that reaches 250, wins the race.
# At that point, you have to print that the corresponding legendary item is obtained.
# In the end, print the remaining shards, fragments, and motes in the format:
# "shards: {number_of_shards}
# fragments: {number_of_fragments}
# motes: {number_of_motes}"
# Finally, print the collected junk items in the order of appearance.

materials = {"shards": 0, "fragments": 0, "motes": 0}
legendary_item = False

while not legendary_item:
    items = input().split()
    for i in range(0, len(items), 2):
        quantity = int(items[i])
        mat = items[i + 1].lower()

        if mat not in materials.keys():
            materials[mat] = 0
        materials[mat] += quantity

        if materials["shards"] >= 250:
            print("Shadowmourne obtained!")
            materials["shards"] -= 250
            legendary_item = True
        elif materials["fragments"] >= 250:
            print("Valanyr obtained!")
            materials["fragments"] -= 250
            legendary_item = True
        elif materials["motes"] >= 250:
            print("Dragonwrath obtained!")
            materials["motes"] -= 250
            legendary_item = True

        if legendary_item:
            break

for key, value in materials.items():
    print(f"{key}: {value}")
