import requests
import datetime
import json
import os

API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
cities = {
    'Tokyo': '1850147',
    'Delhi': '1273294',
    'Berlin': '2950159',
    'London': '2643743',
    'Zurich': '2657896'
}

def get_weather(city_id):
    url = f'http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={API_KEY}'
    response = requests.get(url)
    return response.json()

def main():
    weather_data = {}
    for city, city_id in cities.items():
        weather = get_weather(city_id)
        weather_data[city] = {
            'temperature': weather['main']['temp'],
            'description': weather['weather'][0]['description'],
            'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    with open('weather.json', 'w') as f:
        json.dump(weather_data, f, indent=4)

if __name__ == "__main__":
    main()
