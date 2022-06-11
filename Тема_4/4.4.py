my_list = [9, 7, 3, 7, 7, 10, 10, 3, 6, 10]
no_repeat = []

for i in my_list:
    if i not in no_repeat:
       no_repeat.append(i)
print(no_repeat)


# Другой вариант с использованием множества

# my_set = set(my_list)
# my_list = list(my_set)
#
# print(my_list)
