def filter_list(l):
    lst =[]
    for x in l:
        if type(x) != str:
            lst.append(x)
    return lst