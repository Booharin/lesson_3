number_first = int(input("Введите первое число: "))
number_second = int(input("Введите второе число: "))
number_third = int(input("Введите третье число: "))


def my_func(*args):
    my_list = list(args)
    my_list.sort()
    if len(my_list) > 2:
        print(my_list[-2] + my_list[-1])


my_func(number_first, number_second, number_third)
