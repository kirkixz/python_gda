a = int(input("Первая сторона: "))
b = int(input("Вторая сторона: "))
c = int(input("Третья сторона: "))

if (a + b > c) and (b + c > a) and (a + c > b):
    print("Существует")
else:
    print("Не существует")