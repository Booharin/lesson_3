def my_fun(x, y):
    print(x ** y)


my_fun(2, -4)


def my_pow(x, y):
    if y == 0:
        return 1
    if y == -1:
        return 1 / x
    p = my_pow(x, y // 2)
    p *= p
    if y % 2:
        p *= x
    return p


print(my_pow(2, -4))
