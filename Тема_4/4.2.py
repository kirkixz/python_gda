list1 = [5, 10, 15, 20, 25, 50, 20, 20, 20, 20]

count = list1.count(20)

for i in range(count):
    a = list1.index(20)
    list1[a] = 200

print(list1)