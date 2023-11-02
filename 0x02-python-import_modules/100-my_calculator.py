#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    lenght = len(argv)

    if lenght < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    sign = argv[2]
    if sign == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        exit(0)
    elif sign == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        exit(0)
    elif sign == "/":
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        exit(0)
    elif sign == "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
