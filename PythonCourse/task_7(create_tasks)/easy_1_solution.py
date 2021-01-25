# In a farming-simulator game, you can buy vehicles for a specific price. As a player, you want to buy the
# most expensive vehicle. Here are the vehicles and their prices:
#
# Vehicle: Price
#
# Bicycle: 500
#
# Pickup: 15000
#
# Light Tractor: 35000
#
# Medium Tractor: 45000
#
# Heavy Tractor: 55000
#
# Write a program that determines what is the most expensive vehicle that the user can buy with their money and how
# many of them they can buy.
#
#
# The input format:
#
# How much money user has.
#
# The output format:
#
# How many vehicles the user can afford, for example, 20 bicycles. If the user cannot afford any vehicle, write Zero.

# Sample Input 1:
#
# 18000
# Sample Output 1:
#
# 1 pickup
# Sample Input 2:
#
# 134
# Sample Output 2:
#
# Zero
# Sample Input 3:
#
# 10000
# Sample Output 3:
#
# 20 bicycles

def vehicle_prices(money):
    if money >= 55000:
        print(money // 55000, "heavy tractor" if money // 55000 == 1 else "heavy tractors")
    elif money >= 45000:
        print(money // 45000, "medium tractor" if money // 45000 == 1 else "medium tractors")
    elif money >= 35000:
        print(money // 35000, "light tractor" if money // 35000 == 1 else "light tractors")
    elif money >= 15000:
        print(money // 15000, "pickup" if money // 15000 == 1 else "pickups")
    elif money >= 500:
        print(money // 500, "bicycle" if money // 500 == 1 else "bicycles")
    else:
        print("Zero")


if __name__ == '__main__':
    coins = int(input())
    vehicle_prices(coins)
