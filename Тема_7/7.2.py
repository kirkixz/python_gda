def read_last(lines, file):
    with open(file=file, mode='r', encoding='utf-8') as f:
        text = f.readlines()
        text.reverse()

        for i in range(lines):
            print(text[i].strip())


read_last(5, r"C:\Users\user\Desktop\data.txt")
