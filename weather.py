import requests

class Weather():

    def __init__(self, city, units=None):
        self.city = city
        self.api = '857da17a4a663a880b6369b38ecd6501'
        self.units = units

    def run(self):
        if self.units == None:
            self.units = ''
        else:
            self.units = f"&units={self.units}"
        req_link = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api}{self.units}"
        result = requests.get(req_link).json()
        return result

    def quick_run(self, units='metric'):
        if self.city == "":
            pass
        else:
            try:
                self.units = units
                result = self.run()
                status = result['weather'][0]['description']
                temp_dic = result['main']
                temp = temp_dic['temp']
                feel_temp = temp_dic['feels_like']
                max_temp = temp_dic['temp_max']
                min_temp = temp_dic['temp_min']
                pressure = temp_dic['pressure']
                humidity = temp_dic['humidity']
                wind_speed = result['wind']['speed']

                output = f"{status}\nTemperature is {temp}C\u00B0 \nfeels like: {feel_temp}C\u00B0 \nTemperature range: {min_temp}C\u00B0 - {max_temp}C\u00B0 \nPressure: {pressure} hPa\nHumidity: {humidity}%\nWind speed: {int(wind_speed*60*60/1000)} km h\u207B\u00B9"

            except Exception as e:
                error = self.run()
                output = f"something went wrong\n{error}\n{e}"

            return output