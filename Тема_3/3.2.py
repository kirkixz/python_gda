password = 'qwerty'
print("Нажмите «q», чтобы закончить ввод")
while True:
    value = input("Введите пароль: ")
    if value == "q" or value == "Q" or value == "qwerty":
        break
    else:
        continue
