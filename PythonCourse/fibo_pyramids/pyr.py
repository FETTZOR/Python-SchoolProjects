def fibonacci(number):
    n_1, n_2, n_3, my_list = 1, 0, 0, []
    series = 0
    for loop_it in range(number):
        my_list.append(n_3)
        n_3 = n_1 + n_2
        n_1 = n_2
        n_2 = n_3
        series = series + 1
        for i in range(0, 1):
            for j in range(0, i + 1):
                print('series until', series, '', my_list, end="")

            print("\n")
    return my_list


fibonacci_100 = fibonacci(100)

