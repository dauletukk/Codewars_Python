def is_triangle(a, b, c):
    sum = a + b + c
    m = max(a, b, c)
    return m > sum - m


print(is_triangle(1, 1, 1))
