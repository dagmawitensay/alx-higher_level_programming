#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    number = 0
    if len(roman_string) == 1:
        return romans[roman_string]
    while i + 1 <= len(roman_string):
        try:
            if (romans[roman_string[i]] < romans[roman_string[i + 1]]):
                number += romans[roman_string[i + 1]] - romans[roman_string[i]]
                i += 2
            else:
                number += romans[roman_string[i]]
                i += 1
        except Exception:
            number += romans[roman_string[i]]
            i += 1
    return number
