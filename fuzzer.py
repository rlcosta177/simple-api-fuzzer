import requests
import sys

for word in sys.stdin:
    res = requests.get(url=f"https://pokeapi.co/api/v2/{word}")
    print(res) # response == <Response [200]> OR <Response [404]>
    data = res.json() # show all the data from the API as JSON
    print(data)