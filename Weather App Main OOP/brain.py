import requests
from datetime import datetime

API_KEY = 'e5ac26052ee645b1a5e25946230601'

DATE_API_KEY = 'd55d42ab6fdc4e55a0bfba27274e46a5'



class Data:
    """
    This class hold all the data needed for the application and has methods for requesting the data from the Api and a
    decision system to decide the images that would be displayed depending on the time of the day.
    """
    def __init__(self):
        self.city_name = ''
        self.avg_temp = ''
        self.six_am = ''
        self.nine_am = ''
        self.twelve_pm = ''
        self.three_pm = ''
        self.hourly_weather = ''
        self.tz_id = ''
        self.hr = 0
        self.date = ''
        self.time = ''
        self.sunrise = 0
        self.sunset = 0

        # conditions for the main weather image
        self.weather_condition_main = {
            "Sunny": 'images/sun.png',
            "Cloudy": "images/cloud.png",
            "Partly cloudy": 'images/partly-cloudy.png',
            "rain": 'images/rain.png',
            "snow": 'images/snow.png',
            'Overcast': "images/cloud.png"
        }

        # conditions for the main weather image
        self.weather_condition_small = {
            "Sunny": 'images/113.png',
            "Cloudy": "images/116.png",
            'cloud'
            "Partly cloudy": 'images/119.png',
            "rain": 'images/308.png',
            "snow": 'images/338.png',
            "drizzle": 'images/308.png',
            'sleet': 'images/338.png',
            'Overcast': 'images/119.png'
        }


    def get_city(self, city: str) -> dict:
        """ This method requests and returns the weather data for a particular city. The city is determined by
        passing the keyword argument "city". """
        parameters = {
            'key': API_KEY,
            'q': city
        }
        data = requests.get('http://api.weatherapi.com/v1/forecast.json', params=parameters).json()
        self.city_name = f"{data['location']['name']}"
        self.avg_temp = f'{data["forecast"]["forecastday"][0]["day"]["avgtemp_c"]}°'
        self.six_am = f'{data["forecast"]["forecastday"][0]["hour"][6]["condition"]["text"]}°'
        self.nine_am = f'{data["forecast"]["forecastday"][0]["hour"][9]["condition"]["text"]}°'
        self.twelve_pm = f'{data["forecast"]["forecastday"][0]["hour"][12]["condition"]["text"]}°'
        self.three_pm = f'{data["forecast"]["forecastday"][0]["hour"][15]["condition"]["text"]}°'
        self.tz_id = f"{data['location']['tz_id']}"
        self.sunrise = int(data['forecast']['forecastday'][0]['astro']['sunrise'][0:2])
        self.sunset = int(data['forecast']['forecastday'][0]['astro']['sunset'][0:2]) + 12
        return data



    def get_time(self):
        """ This method requests the time for timezone of the selected city using the tz_id attribute"""
        parameter = {
            'apiKey': DATE_API_KEY,
            'tz': self.tz_id
        }

        data = requests.get("https://api.ipgeolocation.io/timezone", params=parameter).json()
        self.date = data["date_time_txt"][:-15]
        self.hr = int(data["time_24"][:2])
        def pm_or_am(time):
            if time >= 12:
                time_suffix = 'PM'
            else:
                time_suffix = 'AM'

            return time_suffix
        self.time = f'{data["time_24"][:-3]} {pm_or_am(self.hr)}'


    def weather_symbol(self, current_weather: str, size: str) -> str:
        """ This method is the decision system of the weather app. Based on the Keyword arguments provided it determines
        the images to be displayed i.e Sun during the day and moon at night."""
        weather_img = ''
        if size == "big":
            if self.sunset > self.hr and self.sunrise < self.hr:
                for key, value in self.weather_condition_main.items():
                    if key in current_weather:
                        weather_img = self.weather_condition_main[key]
                    else:
                        weather_img = 'images/partly-cloudy.png'
            else:
                weather_img = 'images/crescent.png'
        else:
            for key, value in self.weather_condition_small.items():
                if key in current_weather:
                    weather_img = self.weather_condition_small[key]
                elif 'rain' in current_weather:
                    weather_img = 'images/308.png'
                else:
                    weather_img = 'images/116.png'


        return weather_img


    def get_bg_colour(self) -> str:
        """decision system for background colour depending on time of day."""
        if self.sunset > self.hr >= self.sunrise:
            BG_2 = '#B8E8FC'
        else:
            BG_2 = '#3B3486'
        return BG_2




