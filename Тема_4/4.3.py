list1 = ["Mike", "", "Emma", "Kelly", "", "Brad", "", "", ""]

count = list1.count("")

for i in range(count):
    list1.remove("")

print(list1)