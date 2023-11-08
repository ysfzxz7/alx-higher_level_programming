#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    max_key = max(a_dictionary, key=lambda key: a_dictionary[key])
    return max_key
