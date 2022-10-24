class ListWorker:
    def __init__(self, *args):
        self.args = args
        self.lst = []

    # Метод, который возвращает только числа
    def print_nums(self):
        for value in self.args:
            if isinstance(value, (int, float)):
                self.lst.append(value)
        return self.lst

    # Метод, который возвращает только числа
    def print_str(self):
        for value in self.args:
            if isinstance(value, str):
                self.lst.append(value)
        return self.lst

# Метод, который возвращвет все кроме чисел и строк
    def print_other(self):
        for value in self.args:
            if not isinstance(value, (int, float, str)):
                self.lst.append(value)
        return self.lst


print(ListWorker(1, 2, 3, 4, 5, 's', 'str', 'num', 'raw', [1, 2, 3, '&', 'f'], (2, 5, 'h'), {'wer': 54, 'raw': 65}).print_nums())
print(ListWorker(1, 2, 3, 4, 5, 's', 'str', 'num', 'raw', [1, 2, 3, '&', 'f'], (2, 5, 'h'), {'wer': 54, 'raw': 65}).print_str())
print(ListWorker(1, 2, 3, 4, 5, 's', 'str', 'num', 'raw', [1, 2, 3, '&', 'f'], (2, 5, 'h'), {'wer': 54, 'raw': 65}).print_other())

# 1, 2, 3, 4, 5,                    #числа
# 's', 'str', 'num', 'raw',         #строки
# [1, 2, 3, '&', 'f'],              #список
# (2, 5, 'h'),                      #кортеж
# {'wer': 54, 'raw': 65}            #словарь

# example = 1, 2, 3, 4, 5, 's', 'str', 'num', 'raw', [1, 2, 3, '&', 'f'], (2, 5, 'h'), {'wer': 54, 'raw': 65}
