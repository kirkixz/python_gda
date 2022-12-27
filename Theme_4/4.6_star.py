word_inputted = []
while True:
    content = input()

    if content == 'q':  #Если вводится q, то цикл прерывается
        break
    else:
        word_inputted.append(content)

empty = word_inputted.count('')  #Высчитываем количество пустых строчек

for _ in range(empty):     #Удаляем их
    word_inputted.remove('')

print(word_inputted)
