#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    total = 0
    roman_d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman_list = list(roman_string)
    prev_char = None
    for char in roman_list:
        if prev_char and roman_d[char] > roman_d[prev_char]:
            total += roman_d[char] - 2 * roman_d[prev_char]
        else:
            total += roman_d[char]
        prev_char = char
    return total
