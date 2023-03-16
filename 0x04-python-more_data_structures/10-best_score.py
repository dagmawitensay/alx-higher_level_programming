#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    max_score = 0
    scorer = ""
    for i, j in a_dictionary.items():
        if j > max_score:
            max_score = j
            scorer = i
    return scorer
