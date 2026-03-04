from flask import Flask, render_template, request
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

if __name__ == '__main__':
    app.run(debug=True)