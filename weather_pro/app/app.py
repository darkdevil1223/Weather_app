import requests
api_key = '67b3f37d64723aff149e9e34129f2b06'

city = input("Enter city: ")

wether = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

# print(wether.json())

wed = wether.json()['weather'][0]['description']
temp = wether.json()['main']['temp']
hum = wether.json()['main']['humidity']
loc = wether.json()['name']
cl = (temp - 32)*5/9

# print(wed, cl, hum)
print(f"Todays weather is {wed}")
print(f"Tempratre is {cl}'C")
print(f"humidity is {hum}")