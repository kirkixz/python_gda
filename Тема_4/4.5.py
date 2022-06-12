lst1 = ['Санкт-Петербург', 'Москва', 'Казань']
lst2= ['Воронеж', 'Санкт-Петербург', 'Иваново']
twice = []
once = []


# Создайте 2 списка :
# список только с городами, которые есть в обоих списках;

for i in lst1:
    if i in lst2:
        twice.append(i)

print(f'Эти элементы встречаются в обоих списках:')
for t in twice:
    print(t)
print()




# Список с городами, которые есть только в одном из списков.

for i in lst1:
    if i not in once:
        once.append(i)
for j in lst2:
    if j not in once:
        once.append(j)
    else:
        ind = once.index(j)
        once.pop(ind)

print(f'Эти элементы встречаются единожды в списках:')
for o in once:
    print(o)