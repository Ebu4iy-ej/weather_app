import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import requests

# ключи
TELEGRAM_TOKEN = 'XXXXXXXX'
WEATHER_API_KEY = 'XXXXXXXX'

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    # Создаем кнопку для отправки геолокации
    kb = [
        [types.KeyboardButton(text="📍 Узнать погоду рядом", request_location=True)]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Привет! Нажми на кнопку, чтобы я узнал погоду в твоем месте или напиши свой город.", reply_markup=keyboard)

# Обработка локации
@dp.message(lambda message: message.location is not None)
async def handle_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    
    # Твоя логика запроса к OpenWeather
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    data = requests.get(url).json()
    
    city = data.get('name', 'Неизвестно')
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    
    await message.answer(f"📍 Вы находитесь в: {city}\n🌡 Температура: {temp}°C\n☁️ На улице: {desc}")

    # Обработка текстовых сообщений (названия городов)
@dp.message()
async def handle_city_name(message: types.Message):
    # Если пользователь прислал текст (а не локацию)
    city_name = message.text
    
    # Запрос к API по названию города
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        city = data.get('name')
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        
        # Ссылка на твой сайт (замени на свою реальную ссылку)
        site_url = "https://weather-app-ntgv.onrender.com"
        
        text = (
            f"🌤 Погода в {city}:\n"
            f"🌡 Температура: {temp}°C\n"
            f"📖 Описание: {desc}\n\n"
            f"🔗 Больше деталей на сайте: {site_url}"
        )
        await message.answer(text)
    else:
        await message.answer("❌ Город не найден. Попробуй еще раз!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
