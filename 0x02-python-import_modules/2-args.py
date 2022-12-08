#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv[1:]
    count = len(arg)
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
        for i in range(count):
            print("{}: {}".format(i + 1, arg[i]))
    else:
        print("{} arguments:".format(count))
        for i in range(count):
            print("{}: {}".format(i + 1, arg[i]))
