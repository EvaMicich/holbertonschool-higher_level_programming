#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    total = 0
    for i in range(len(roman_string)):
        if roman_string[i] == "I":
            total += 1
        if roman_string[i] == "V":
            if i > 0 and roman_string[i - 1] == "I":
                total -= 2
            total += 5
        if roman_string[i] == "X":
            if i > 0 and roman_string[i - 1] == "I":
                total -= 2
            total += 10
        if roman_string[i] == "L":
            if i > 0 and roman_string[i - 1] == "X":
                total -= 20
            total += 50
        if roman_string[i] == "C":
            if i > 0 and roman_string[i - 1] == "X":
                total -= 20
            total += 100
        if roman_string[i] == "D":
            if i > 0 and roman_string[i - 1] == "C":
                total -= 200
            total += 500
    return total
