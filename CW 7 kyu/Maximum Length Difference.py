# You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. Let x be any
# string in the first array and y be any string in the second array.
#
# Find max(abs(length(x) − length(y)))
#
# If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).
#
# #Example:
#
# a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
# a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
# mxdiflg(a1, a2) --> 13


def mxdiflg(a1, a2):
    if not (a1 and a2): return -1
    l1 = list(map(len, a1))
    l2 = list(map(len, a2))
    print(l1)
    print(l2)
    return max((max(l1) - min(l2)), (max(l2) - min(l1)))


print(mxdiflg(["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"],
          ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]))
