#!/usr/bin/python3
if __name__ == "__main__":
    import sys, hidden_4
    for name in dir(hidden_4):
        if name[0:2] != "__":
            print(name)
