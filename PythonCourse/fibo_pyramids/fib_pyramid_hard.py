import sys
import statistics

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
                summa = sum(my_list)
                median = round(statistics.median(my_list))
                average = round(sum(my_list) / len(my_list))
                str1 = " "
                d = str1.join(map(str, my_list))
                print(f'series until {series}'',['+d, end=f"],{summa},{median},{average}")
            print()

    return my_list



fibonacci(100)
if __name__ == '__main__':

    original_stdout = sys.stdout

    print('')
    with open('fibonacci.csv', 'w') as f:
        sys.stdout = f
        fibonacci(100)
        sys.stdout = original_stdout