import requests

def get_weather(city = None, lat=None, lon=None):
    api_key = 'XXXXXXXX'
    if lat and lon:
        # Если есть координаты, строим ссылку по ним
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=ru"
    else:
        # Иначе ищем по названию города
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru'

    response = requests.get(url)
    data = response.json()

 # Проверяем, всё ли хорошо
    if data.get('cod') == 200:
        # Возвращаем словарь с самыми важными данными
        return{
            'main': data['weather'][0]['main'],
            'city': data['name'],
            'temp': data['main']['temp'],
            'desc': data['weather'][0]['description'],
            'feels_like': data['main']['feels_like'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
    else:
        # Если город не найден, возвращаем None (ничего)
        return None

#city = (input('Город '))

def get_forecast(city):
    api_key = '1679f5ca7ac79ae9838dc130c6e24a43'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric&lang=ru'

    response = requests.get(url)
    data = response.json()

    if str(data.get('cod')) == '200':
        forecast_list = []
        for day in data['list']:
            ## Проверяем, есть ли в строке времени "12:00:00"
            if '12:00:00' in day['dt_txt']:
                forecast_list.append({
                    'date': day['dt_txt'],
                    'temp': day['main']['temp'],
                    'desc': day['weather'][0]['description']
                })
        return forecast_list
        











'''api_key = '1679f5ca7ac79ae9838dc130c6e24a43'
user_city = (input('Введите ваш город: '))
# Собираем ссылку с помощью f-строки
url = f'https://api.openweathermap.org/data/2.5/weather?q={user_city}&appid={api_key}&units=metric&lang=ru'
response = requests.get(url)
# Выводим результат в формате JSON
#print(response.json())
data = response.json()
if data.get('cod') == 200:
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    description = data['weather'][0]['description']

    print(f'Погода в городе {user_city}:')
    print(f'Температура: {temp} °C')
    print(f'На небе сейчас: {description}')
else:
    print('Ошибка город не найден.')'''

