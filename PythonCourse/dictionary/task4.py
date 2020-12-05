import random

constants = {
    'pi': 3.14,
    'e': 2.71,
    'sqrt': 1.14,
    # etc :D
}
print(list(constants.values()))

def random_divided_random_const():
    random_int = random.randint(0, 200)
    print("random int", random_int)
    divider = random.choice(list(constants.values()))
    print("divider", divider)
    result = random_int / divider
    return result


print(random_divided_random_const())
# a = 5.5
# b = 5
# is_a_close_to_b = abs(a-b) < 1.0 # Returns True if difference between a and b is less than 1.0
