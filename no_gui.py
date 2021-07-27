import weather

city = input("Enter your location: ")
get_weather = weather.Weather(city)
result = get_weather.quick_run()
print(result)