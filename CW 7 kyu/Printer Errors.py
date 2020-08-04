# https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python

def printer_error(s):
    count = 0
    for i in s:
        if i not in 'abcdefghijklm':
            count +=1
    return str(count)+"/"+str(len(s))