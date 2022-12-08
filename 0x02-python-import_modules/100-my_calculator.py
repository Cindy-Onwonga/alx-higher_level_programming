#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    arg = sys.argv[1:]
    count = len(arg)
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if arg[1] != '+' and arg[1] != '-' and arg[1] != '*' and arg[1] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        a = int(arg[0])
        b = int(arg[2])
        if arg[1] == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif arg[1] == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif arg[1] == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif arg[1] == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
