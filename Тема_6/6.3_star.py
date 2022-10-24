class Nikola:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        if name == 'Николай':
            print(f"Николай, {age} лет")
        else:
            print(f"Я не {name}, а Николай и мне {age} лет")


andrew = Nikola('Андрей', 19)
nikola = Nikola('Николай', 20)