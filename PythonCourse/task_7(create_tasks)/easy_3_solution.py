# You need to write a program that converts miles to kilometers.
# In this program, you should:
#
# 1. Round values to one decimal place. Like (2.333333 = 2.33)
# 2. Write 3 functions. Where one of them converting miles to km, second km to mi(miles)
# and 3rd call the necessary function depending on what was given in the input(in mi or in km)
# 3. Print the converted speed value with the new unit
# 4. On wrong input says Wrong input, please, try again!

# Sample input / output
# Enter value>? 2
# Wrong input, please, try again!
# Enter value>? 1 km
# 0.62 miles


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
