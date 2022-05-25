counter = 0
print("Нажмите «q», чтобы закончить ввод")
while True:
    value = input("Введите значение: ")
    if value == "q" or value == "Q":
        break
    else:
        if int(value) % 2 == 0:
            counter += 1
print(f"Вы ввели {counter} четных чисел")