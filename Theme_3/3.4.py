# С помощью условного оператора if   1 до 1000000

for i in range(1, 1000000):
    if i % 2 == 0:
        print(i)


# Без использования условного оператора if

for i in range(1, 1000000, 2):
    print(i-1)

# Или так

for i in range(0, 1000000, 2):
    print(i)

