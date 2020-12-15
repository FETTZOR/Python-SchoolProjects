import statistics


def fibonacci(number):
    n_1, n_2, n_3, my_list = 1, 0, 0, []
    for loop_it in range(number):
        my_list.append(n_3)
        n_3 = n_1 + n_2
        n_1 = n_2
        n_2 = n_3
    return my_list


fibonacci_200 = fibonacci(200)
print(fibonacci_200)
fibonacci_70 = fibonacci(70)
print(fibonacci_70)
