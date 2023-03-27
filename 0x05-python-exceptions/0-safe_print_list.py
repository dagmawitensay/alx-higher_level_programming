#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ctr = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            ctr += 1
    except IndexError:
        print()
        return ctr
    else:
        print()
        return ctr
