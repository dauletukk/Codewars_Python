def toJadenCase(string):
    s = ""
    for i in string.split():
        s += i[0].upper() + i[1:] + " "
    return s

print(toJadenCase("How can mirrors be real if our eyes aren't real"))