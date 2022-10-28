def print_last_ln(lines, path):
    with open(file=path, mode='r', encoding='utf-8') as f:
        text = f.readlines()
        text.reverse()

        for i in range(lines):
            print(text[i].strip())


print_last_ln(5, r"C:\Users\user\Desktop\data.txt")
