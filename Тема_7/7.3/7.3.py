def print_long_word(file):
    with open(file=file, mode='r', encoding='utf-8') as f:
        text = f.readlines()
        max_len = 0
        lst = []

        for j in text:
            if len(j) > max_len:
                max_len = len(j)

        for i in text:
            if len(i) == max_len:
                lst.append(i.rstrip('\n\r'))

    print(lst[0] if len(lst) == 1 else lst)


print_long_word('data.txt')
