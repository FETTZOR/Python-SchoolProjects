def vehicle_prices(money):
    if money >= 6769:
        print(money // 6769, "heavy tractor" if money // 6769 == 1 else "heavy tractors")
    elif money >= 3848:
        print(money // 3848, "medium tractor" if money // 3848 == 1 else "medium tractors")
    elif money >= 1296:
        print(money // 1296, "light tractor" if money // 1296 == 1 else "light tractors")
    elif money >= 678:
        print(money // 678, "pickup" if money // 678 == 1 else "pickups")
    elif money >= 23:
        print(money // 23, "bicycle" if money // 23 == 1 else "bicycles")
    else:
        print("None")


if __name__ == '__main__':
    coins = int(input())
    vehicle_prices(coins)
