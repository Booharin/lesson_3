def my_func():
    my_string = ""
    my_sum = 0

    while '$' not in my_string:
        my_string = input("Введите строку с числами, разделенными пробелами, для отмены введите '$': ")
        my_list = my_string.split()
        my_int_list = []
        for i in my_list:
            try:
                my_int_list.append(int(i))
            except ValueError:
                my_int_list.append(i)

        print(my_int_list)
        for i in my_int_list:
            if i == '$':
                print(my_sum)
                return
            else:
                my_sum += i
        print(my_sum)


my_func()
