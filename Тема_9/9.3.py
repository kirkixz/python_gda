import requests

r = requests.get("https://github.com/search?q=language:Python&type=Repositories")
link = "https://github.com/search?q=language:Python&type=Repositories"

print(r.text.find("Showing"))
print(link)

