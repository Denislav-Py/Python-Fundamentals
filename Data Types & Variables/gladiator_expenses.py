# As a gladiator, Peter needs to repair his broken equipment when he loses a fight. His equipment consists of a helmet, a sword, a shield, and armor.
# You will receive Peter's lost fights count.
# Every second lost game, his helmet is broken.
# Every third lost game, his sword is broken.
# When both his sword and helmet are broken in the same lost fight, his shield also breaks.
# Every second time his shield breaks, his armor also needs to be repaired.
# You will receive the price of each item in his equipment. Calculate his expenses for the year for renewing his equipment.

number_of_losses = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helms_broken = number_of_losses // 2
swords_broken = number_of_losses // 3
shields_broken = number_of_losses // (2 * 3)
armor_broken = shields_broken // 2

total_expenses = helms_broken * helmet_price + swords_broken * sword_price + shields_broken * shield_price + \
                 armor_broken * armor_price

print(f"Gladiator expenses: {total_expenses:.2f} aureus")
