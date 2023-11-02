#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    lenght = len(argv)
    i = 1

    if lenght == 1:
        print("{} arguments.".format(lenght - 1))
    if lenght > 1:
        if lenght == 2:
            print("{} argument:".format(lenght -1))
            print("1: {}".format(argv[1]))
        else:
            print("{} arguments:".format(lenght))
            while i < lenght:
                print("{:d} : {}".format(i, argv[i]))
                i += 1
