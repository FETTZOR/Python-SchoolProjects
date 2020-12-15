import sys


def fibonacci(number):
    n_1, n_2, n_3, my_list = 1, 0, 0, []
    series = 0
    print('fibonacci series from 1 to 100')
    for loop_it in range(number):
        my_list.append(n_3)
        n_3 = n_1 + n_2
        n_1 = n_2
        n_2 = n_3
        series = series + 1
        for i in range(0, 1):
            for j in range(0, i + 1):
                print('series until', series, '', my_list, end="")
            print()
    return my_list

fibonacci(100)
if __name__ == '__main__':

    original_stdout = sys.stdout

    print('')
    with open('fibonacci_series.txt', 'w') as f:
        sys.stdout = f
        fibonacci(100)
        sys.stdout = original_stdout

