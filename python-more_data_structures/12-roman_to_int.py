#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    total = 0
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman_list = list(roman_string)
    prev_char = None
    for char in roman_list:
        if prev_char and roman_dict[char] > roman_dict[prev_char]:
            total += roman_dict[char] - 2 * roman_dict[prev_char]
        else:
            total += roman_dict[char]
        prev_char = char
    return total
