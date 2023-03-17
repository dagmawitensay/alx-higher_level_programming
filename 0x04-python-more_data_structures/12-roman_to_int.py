#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0

    for i in range(len(roman_string)):
        if i + 1 < len(
                roman_string
                ) and romans[roman_string[i]] < romans[roman_string[i + 1]]:
            number -= romans[roman_string[i]]
        else:
            number += romans[roman_string[i]]

    return number
