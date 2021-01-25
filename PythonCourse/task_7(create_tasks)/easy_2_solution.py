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
