#!/usr/bin/python3


def multiple_returns(sentence):
    fi = ""
    if len(sentence) == 0:
        fi = None
    fi = sentence[0]
    tuple_r = (len(sentence), fi)
    return tuple_r
