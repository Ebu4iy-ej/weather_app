from flask import Flask, render_template, request, jsonify
from weather import get_weather, get_forecast # Импортируем твою функцию!

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    weather_data_forecast = None
    if request.method == 'POST':
        city = request.form.get('city')
        # Вызываем твою функцию
        weather_data = get_weather(city)
        weather_data_forecast = get_forecast(city)
    return render_template('index.html', weather=weather_data, weather_forecast=weather_data_forecast)

@app.route('/weather_by_coords', methods=['POST'])
def weather_by_coords():
    weather_by_coords = None
    if request.method == 'POST':
        coords = request.get_json()
        # 1. Получаем данные (JSON) из запроса
        request.get_json()
         # 2. Вызываем get_weather с полученными lat и lon
        weather_by_coords = get_weather(lat=coords['lat'], lon=coords['lon'])
        # 3. Возвращаем результат обратно в браузер
    return jsonify(weather_by_coords)

import subprocess
import os

# Этот код запустит бота как отдельный процесс прямо из Flask
if os.environ.get('RENDER'): # Проверка, что мы на хостинге
    subprocess.Popen(["python", "bot.py"])

if __name__ == '__main__':
    app.run(debug=True)