#!/usr/bin/python3
""" This is the Plane program made by Felix Beniamin Cenusa BTH student Software Engineering 2023-2026 """
height_over_sea_metric = float(input("Height over the sea (meters): "))
speed_metric = float(input("Speed (km/h): "))
temperature_metric = float(input("Temperature (celcius): "))

#Convertng to Imperial units

height_over_sea_imperial = height_over_sea_metric * 3.280839895
speed_imperial = speed_metric * 0.621371
temperature_imperial = temperature_metric * 9 / 5 + 32

print("Height over the sea (feet): ", round(height_over_sea_imperial, 2))
print("Speed (mph): ", round(speed_imperial, 2))
print("Temperature (farenheit): ", round(temperature_imperial, 2))
