#!/usr/bin/python3
def uppersace(str):
    for i in str:
        if ord(i) >=ord('a') and ord(i) <= ord('z'):
            i = chr(ord(i) - 32)
    print("{:c}".format(i), end="")
    print()
