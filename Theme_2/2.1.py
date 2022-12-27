temperature_room = float(input("Введите температуру в комнате "))
desired_temperature = float(input("Введите желаемую температуру "))
humidity_air = int(input("Введите влажность воздуха "))

if temperature_room > desired_temperature and humidity_air < 80:
    print("on")
else:
    print("off")