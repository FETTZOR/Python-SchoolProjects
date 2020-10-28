#! /usr/bin/python3

def list_to_sum(list_to_sum_input):
    sum_to_return = 0
    for i in range(len(list_to_sum_input)):
        sum_to_return = sum_to_return + list_to_sum_input[i]
    return sum_to_return


sum_answer = list_to_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(sum_answer)
