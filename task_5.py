def my_func():
    my_string = input("Введите строку с числами, разделенными пробелами, для отмены введите $ ")
    while '$' not in my_string:
        print(my_string)
