def perimeter(a=0, b=0, c=0, d=0):
    return f'Периметр: {a + b + c + d}'


a = int(input('Сторона четырехугольника a: '))
b = int(input('Сторона четырехугольника b: '))
c = int(input('Сторона четырехугольника c: '))
d = int(input('Сторона четырехугольника d: '))

print(perimeter(a, b, c, d))
