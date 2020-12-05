
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
    return [my_list, sum(my_list), my_list[-1]]

fibonacci_200 = fibonacci(200)
print(fibonacci_200)
fibonacci_70 = fibonacci(70)
print(fibonacci_70)

# Make a function that returns a list where first element is a list of numbers of the Fibonacci series second element is sum
# of the series and last element is last element on the series, argument to the function is number of numbers in series.