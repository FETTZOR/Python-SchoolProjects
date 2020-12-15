import statistics


def fibonacci(number):
    w = number // 2
    my_list = []
    x = 0
    y = 1
    for a in range(w):
        my_list.append(x)
        my_list.append(y)
        x = x + y
        y = y + x
    my_tuple = tuple(my_list)
    return [my_tuple, sum(my_list), my_list[-1], statistics.median(my_list), "Milla Jovovich",
            sum(my_list) / len(my_list)]


fibonacci_200 = fibonacci(200)
print(fibonacci_200)
fibonacci_70 = fibonacci(70)
print(fibonacci_70)

# Make a function that returns a list where the first element is a tuple of numbers of the Fibonacci series, the second element is
# the sum of the series, the third element is a last element on the series, the fourth element is a median value in the series,
# the fifth element is naturally a string "Milla Jovovich", the sixt element is a average of the series. Argument to function is number of numbers in series.
