# Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.
#
# For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.
#
# The input will be a lowercase string with no spaces.
#
# Good luck!
#
# If you like this Kata, please try:
#
# Indexed capitalization
#
# Even-odd disparity

def capitalize(s):
    res = ['','']
    for index,val in enumerate(s):
        res[0] += val.lower() if index % 2 else val.upper()
        res[1] += val.upper() if index % 2 else val.lower()
    return res