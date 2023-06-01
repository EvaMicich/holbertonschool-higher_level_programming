#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if 97 <= ord(str[i]) <= 122:
            upper = chr(ord(str[i]) - 32)
            print("{}".format(upper), end="")
        else:
            print("{}".format(str[i]), end="")
    print("")
