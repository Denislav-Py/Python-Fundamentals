# You will receive a group size. After that, you receive the days of the adventure.
# Every day, you earn 50 coins, but you also spend 2 coins per companion for food.
# Every 3rd (third) day, you organize a motivational party, spending 3 coins per companion for drinking water.
# Every 5th (fifth) day, you slay a boss monster and gain 20 coins per companion. But if you have a motivational party the same day, you spend an additional 2 coins per companion.
# Every 10th (tenth) day at the start of the day, 2 (two) of your companions leave, but every 15th (fifteenth) day 5 (five) new companions are joined at the beginning of the day.
# You should calculate how many coins gets each companion at the end of the adventur
from math import floor

group_size = int(input())
days = int(input())

total_coins = 0

for number in range(1, days + 1):
    if number % 10 == 0:
        group_size -= 2

    if number % 15 == 0:
        group_size += 5

    total_coins += 50
    total_coins -= group_size * 2

    if number % 3 == 0:
        total_coins -= group_size * 3

    if number % 5 == 0:
        total_coins += group_size * 20

    if number % 3 == 0 and number % 5 == 0:
        total_coins -= group_size * 2

print(f"{group_size} companions received {floor(total_coins / group_size)} coins each.")

