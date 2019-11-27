import pyowm
owm = pyowm.OWM('6d00d1d4e704068d70191bad673e0cc')
place = input("Input city?:")

observation = owm.weather_at_place(place)
w = observation.get_weather()
print(w)  