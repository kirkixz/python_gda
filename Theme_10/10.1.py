class DigitException(Exception):
    def __init__(self, text):
        self.text = text


name = input('Введите имя: ')

for var in name:
    if var.isdigit():
        raise DigitException('В имени обнаружена цифра')
else:
    print(name)

