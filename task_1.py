number_first = int(input("Введите первое число: "))
number_second = int(input("Введите второе число: "))


def division(var_1, var_2):
    try:
        print(var_1 / var_2)
    except ZeroDivisionError:
        print("Error zero division")


division(number_first, number_second)
