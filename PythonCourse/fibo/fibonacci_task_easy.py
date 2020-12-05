
def fibonacci(number):
    w = number//2
    my_list = []
    x = 0
    y = 1
    for a in range(w):
        my_list.append(x)
        my_list.append(y)
        x = x + y
        y = y + x
    return my_list

fibonacci_200 = fibonacci(200)
print(fibonacci_200)
fibonacci_70 = fibonacci(70)
print(fibonacci_70)

# Fibonaci series is series of numbers where next number is always sum of two previous numbers
# Make a function that returns a list of numbers of the Fibonacci series, argument to function is number of numbers in series.
# 1,1,2,3,5,8,13,21,34,55
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ...
# xn = xn−1 + xn−2
