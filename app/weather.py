from requests import get
#from datetime import datetime
#fa5d477aae0969e346a711c4f1e44e19
#{'lat': 58.0174, 'lon': 56.2855} (Perm)


class Weather(object):


    def __init__(self):
        self.now_str = get("https://api.openweathermap.org/data/2.5/weather?q=Perm,ru&appid=fa5d477aae0969e346a711c4f1e44e19&units=metric&lang=ru").json()
        self.forecast_str = get("https://api.openweathermap.org/data/2.5/forecast?lat=58.0174&lon=56.2855&appid=fa5d477aae0969e346a711c4f1e44e19&units=metric&lang=ru&cnt=3").json()
    

    def weather_now(self):
        array = self.now_str
        
        weather = {
            'weather_main':array['weather'][0]['description'],
            'temp_now':array['main']['temp'],
            'temp_feels':array['main']['feels_like'],
            'wind_speed':array['wind']['speed'],
            'wind_vect':self.wind_vector(array['wind']['deg'])
        }

        return weather
    

    def weather_fc(self):
        array = self.forecast_str['list'][2]

        forecast = {
            'datetime':array['dt_txt'],
            'weather_main':array['weather'][0]['description'],
            'temp_now':array['main']['temp'],
            'temp_feels':array['main']['feels_like']
        }

        return forecast
    

    def wind_vector(self, deg):
        if deg >= 0 and deg <= 22.5:
            result = "Север"
            return result
        elif deg > 22.5 and deg <= 67.5:
            result = "Северо-Восток"
            return result
        elif deg > 67.5 and deg <= 112.5:
            result = "Восток"
            return result
        elif deg > 112.5 and deg <= 157.5:
            result = "Юго-Восток"
            return result
        elif deg > 157.5 and deg <= 202.5:
            result = "Юг"
            return result
        elif deg > 202.5 and deg <= 247.5:
            result = "Юго-Запад"
            return result
        elif deg > 247.5 and deg <= 292.5:
            result = "Запад"
            return result
        elif deg > 292.5 and deg <= 337.5:
            result = "Северо-Запад"
            return result
        elif deg > 337.5:
            result = "Север"
            return result


    def read_arr(self, array):
        for k, v in array.items():
            print("{} - {}".format(k, v))
        
        return 0
