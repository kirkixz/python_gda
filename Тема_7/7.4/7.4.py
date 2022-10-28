def print_word_count(file, search_word) -> int:
    marks = '!();?:,.'
    with open(file=file, mode='r', encoding='utf-8') as f:
        temp = f.readlines()
        counter = 0

        for i in range(len(temp)):
            temp[i] = temp[i].strip().lower().split(' ')

            for j in temp[i]:
                for char in marks:
                    j = j.replace(char, '')
                if j == search_word.lower():
                    print(j)
                    counter += 1

    print(counter)


print_word_count('data.txt', 'Товарищи')
