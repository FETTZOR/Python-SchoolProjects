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
