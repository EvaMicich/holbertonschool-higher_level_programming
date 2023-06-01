#!/usr/bin/python3
for a in range(9):
    b = a + 1
    while b <= 9:
        if (a * 10 + b) == 89:
            print("{:02d}".format(a * 10 + b), end="\n")
        else:
            print("{:02d}".format(a * 10 + b), end=", ")
        b = b + 1
