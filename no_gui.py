import weather

api = '857da17a4a663a880b6369b38ecd6501'

city = input("Enter your location: ")
get_weather = weather.Weather(city, api)
result = get_weather.quick_run()
print(result)
