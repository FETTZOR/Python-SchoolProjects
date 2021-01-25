def miles_to_km(convert_to_km):
    km = convert_to_km / 0.62137
    return round(km, 2)


def km_to_miles(convert_to_miles):
    miles = convert_to_miles * 0.62137
    return round(miles, 2)


def main():
    try:
        speed_value, unit = input("Enter value").split()
        speed_value = int(speed_value)
        if unit == 'km':
            print(km_to_miles(speed_value), 'miles')
        elif unit == 'mi':
            print(miles_to_km(speed_value), 'kilometres')

    except:
        print("Wrong input, please, try again!")
        main()


if __name__ == '__main__':
    main()
