def get_sum_numbers(first_num: int, second_num: int) -> int | str:
    try:
        sum = first_num + second_num

        return sum

    except TypeError:
        return 'Ожидаемый тип данных — число'

print(get_sum_numbers('t', 5))
print(get_sum_numbers('4', 5))
print(get_sum_numbers(4, 5))
