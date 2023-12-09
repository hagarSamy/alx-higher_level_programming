#!/usr/bin/python3
def best_score(a_dictionary):
    return max(a_dictionary, key=a_dictionary.get) if a_dictionary else None
    # if not a_dictionary:
    # return None
    # max_val = max(a_dictionary.values())
    # best_k = [k for k, v in a_dictionary.items() if v == max_val]
    # return best_k
