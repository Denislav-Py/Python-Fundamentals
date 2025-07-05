# Write a program that keeps the information about products and their prices. Each product has a name, a price, and a quantity:
#
# If the product doesn't exist yet, add it with its starting quantity.
#
# If you receive a product, that already exists, increase its quantity by the input quantity and if its price is different, replace the price as well.
#
# You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy", keep adding items.
# Finally, print all items with their names and the total price of each product.

my_products = {}

while True:
    cmd = input()
    if cmd == "buy":
        break

    data = cmd.split()
    product = data[0]
    price = float(data[1])
    qty = int(data[2])

    if product not in my_products.keys():
        my_products[product] = []
        my_products[product].append(price)
        my_products[product].append(qty)
    else:
        my_products[product][1] += qty
        my_products[product][0] = price

for item in my_products.keys():
    print(f"{item} -> {my_products[item][0] * my_products[item][1]:.2f}")
