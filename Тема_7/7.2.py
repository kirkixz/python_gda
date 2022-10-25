def read_last(lines, file):
    with open(file=file, mode='r', encoding='utf-8') as f:
        # for line in range(-1, -lines - 1, -1):
        #
        #     print(f.readlines()[line])
        for line in range(lines):
            counter = -1
            while counter != -lines:
                print(f.readline()[counter].strip())
                counter = counter - 1
                print(counter)
                break


read_last(3, r"C:\Users\user\Desktop\data.txt")
