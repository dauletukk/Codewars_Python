# Your task is to remove all duplicate words from a string, leaving only single (first) words entries.
#
# Example:
#
# Input:
#
# 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
#
# Output:
#
# 'alpha beta gamma delta'
# Test.it("Basic tests")
# Test.assert_equals(remove_duplicate_words
# ("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"),
# "alpha beta gamma delta")
# Test.assert_equals(remove_duplicate_words("my cat is my cat fat"), "my cat is fat")
# https://www.codewars.com/kata/5b39e3772ae7545f650000fc/train/python

def remove_duplicate_words(s):
    s = s.split(" ")
    lst = []
    for item in s:
        if item not in lst:
            lst.append(item)
    return " ".join(lst)