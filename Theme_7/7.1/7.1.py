def print_six_ln():
    with open(r"C:\Users\user\Desktop\data.txt", mode='r', encoding='utf-8') as f:
        for i in range(6):
            print(f.readline().strip())


print_six_ln()