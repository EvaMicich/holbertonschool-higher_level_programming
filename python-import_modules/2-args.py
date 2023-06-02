#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    if len(sys.argv) == 2:
        print("1 argument:\n1: {}".format(sys.argv[1]))
    if len(sys.argv) > 2:
        print("{} arguments:".format(len(sys.argv)-1))
        for i in range(len(sys.argv)):
            if i == 0:
                continue
            print("{}: {}".format(i, sys.argv[i]))
