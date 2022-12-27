import requests

url = input("Введите интересующий вас URL: ")
r = requests.get(url)

print(f"Код статуса: {r.status_code()}\nURL: <{url}>")
