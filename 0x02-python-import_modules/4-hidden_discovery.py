#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4 as hidd
    vars = dir(hidd)
    for i in vars:
        if i[:2] != '__':
            print("{}".format(i))
