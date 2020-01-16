def int_func(my_string):
    return my_string.title()


print(int_func('text'))

my_new_string = "hello my beautiful world"

my_list = my_new_string.split()

for index, value in enumerate(my_list):
    my_list[index] = int_func(value)

print(" ".join(my_list))