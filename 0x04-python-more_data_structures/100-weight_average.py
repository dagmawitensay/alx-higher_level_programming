#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return None
    total_sum = 0
    div = 0
    for item in my_list:
        total_sum += item[0] * item[1]
        div += item[1]
    return total_sum / div
