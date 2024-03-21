import requests
# import math
def inp(cit):
    global city
    city = cit

def wed_app():

    api_key = '67b3f37d64723aff149e9e34129f2b06'

    # city = input("Enter city: ")
    # city = 'Mumbai'

    wether = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

    # print(wether.json())

    wed = wether.json()['weather'][0]['description']
    spd = wether.json()['wind']['speed']
    temp = wether.json()['main']['temp']
    hum = wether.json()['main']['humidity']
    loc = wether.json()['name']
    tem = (temp - 32)*5/9

    cl = round(tem, 2)

# print(wed, cl, hum)
    print(f"Todays weather is {wed}")
    print(f"Tempratre is {cl}'C")
    print(f"humidity is {hum}")
    print(f"Location is {loc}")
    print(f"wind speed is {spd}")


    return [wed,temp,hum,loc,cl,spd]