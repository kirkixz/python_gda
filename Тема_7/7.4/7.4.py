def print_word_count(file, search_word) -> int:
    marks = '!();?:,.'
    with open(file=file, mode='r', encoding='utf-8') as f:
        text = f.readlines()
        counter = 0

        for i in range(len(text)):
            text[i] = text[i].strip().lower().split(' ')

            for j in text[i]:
                for char in marks:
                    j = j.replace(char, '')
                if j == search_word.lower().strip():
                    counter += 1

    print(counter)


print_word_count('data.txt', 'Товарищи')
