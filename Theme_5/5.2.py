# Данную задачу можно решить двумя способами:
# через *args и через map()


# Через *args, когда мы сами определяем количество значений вбираемых аргументом через вызов функции
def arithmetic_mean(*args):
    res = 0
    counter = 0
    for arg in args:
        res += arg
        counter += 1

    return res / counter


print(arithmetic_mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# Через map(), когда возможный пользователь сам определяет количество значений которое ему надо, не залезая в код,
# а сделав это через терминал, а в будущем может и через графический интерфейс

# def func(arg):
#     res = 0
#     counter = 0
#     for n in arg:
#         res += n
#         counter += 1
#
#     return res / counter
#
#
# input_nums = map(int, input('Введите числа через запятую: ').split(','))   # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#
# print(func(list(input_nums)))
