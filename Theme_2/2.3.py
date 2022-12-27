a = int(input("Первая сторона: "))
b = int(input("Вторая сторона: "))
c = int(input("Третья сторона: "))

if (a == b) or (b == c) or (a == c):
    print("Равнобедренный")
else:
    print("Не равнобедренный")
