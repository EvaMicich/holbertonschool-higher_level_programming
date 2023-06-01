#!/usr/bin/python3
for i in range(26):
    j = chr(97 + i)
    if j == "q" or j == "e":
        continue
    else:
        print("{}".format(j), end="")
