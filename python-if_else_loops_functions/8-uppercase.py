#!/usr/bin/python3

def uppercase(str):
    new = ""
    for i in range(len(str)):
        if 97 <= ord(str[i]) <= 122:
            upper = chr(ord(str[i]) - 32)
            new = new + upper
        else:
            new = new + str[i]
    print("{0}".format(new))
