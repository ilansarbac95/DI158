import requests

chuck_url = "https://api.chucknorris.io/jokes/random?category=dev"

req = requests.get(chuck_url)

info = req.json()

joke = info('value')

print(joke)


