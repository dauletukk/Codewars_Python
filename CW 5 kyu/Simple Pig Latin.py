# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

def pig_it(text):
    txt = []
    for i in text.split():
        if i.isalpha():
            txt.append(i[1:] + i[0] + 'ay')
        else:
            txt.append(i)
    return ' '.join(txt)
