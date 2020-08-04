def get_sum(a, b):
    count = 0
    if a == b:
        return a
    elif a > b:
        for i in range(b, a + 1):
            count += i
        return count
    else:
        for i in range(a, b + 1):
            count += i
        return count


print(get_sum(1, 3))
