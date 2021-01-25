# Pekka decided to make a list of the groceries he needed to buy for dinner.
# To remember their names. Pekka politely asks you to put them in the list. Read the names from the input,
# each on a new line, and stop at exclamation mark !
# that denotes the end of the sequence.
#
# Print your list and return its length (the number of products) for Pekka.

# Sample Input:
#
# carrot
# potato
# cheese
# milk
# !
# Sample Output:
#
# ['carrot', 'potato', 'cheese', 'milk']
# 4


def grocery_list(n):
    groceries = []
    while n == 1:
        names = input("Hello! Please write product name below or write ! to stop the program!: ")
        if names == '!':
            break
        else:
            groceries.append(names)
    print(groceries)
    return len(groceries)


if __name__ == '__main__':
    print(grocery_list(1))
