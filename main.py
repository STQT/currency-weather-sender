import logging
import requests
from datetime import datetime

from telebot import TeleBot, StateMemoryStorage
from telebot.apihelper import ApiTelegramException

from month_translate import formatted_date_uzbek
from config import TOKEN, POGODAS_TOKEN
from utils import iconPhraseToUzbek, get_aqi_description

bot = TeleBot(TOKEN, state_storage=StateMemoryStorage())

current_datetime = datetime.now()


def pogodas_text():
    response = requests.get("https://billboard.mediabaza.uz/api/info/weather/")
    if response.status_code == 200:
        weather_data = response.json()
        
        # Преобразование timestamp в читаемый формат
        sunrise_time = datetime.fromtimestamp(weather_data['sunrise']).strftime('%H:%M')
        sunset_time = datetime.fromtimestamp(weather_data['sunset']).strftime('%H:%M')
        
        # Перевод погодных условий на узбекский
        weather_uzbek = {
            'Clear': 'Ochiq',
            'Clouds': 'Bulutli',
            'Rain': 'Yomg\'irli',
            'Snow': 'Qorli',
            'Thunderstorm': 'Momaqaldiroqli',
            'Drizzle': 'Mayda yomg\'ir',
            'Mist': 'Tumanli',
            'Fog': 'Tumanli',
            'Haze': 'Dumli'
        }.get(weather_data['weather_main'], weather_data['weather_main'])
        
        message = f"""
🌤️ <b>Bugungi ob-havo</b>  
📍 <b>Shahar:</b> Toshkent  
📆 <b>Sana:</b> {datetime.strptime(weather_data['last_updated'], '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%d-%m-%Y')}  
        
🌡️ <b>Harorat:</b>  
- <b>Hozirgi:</b> {weather_data['current_temp']}°C
- <b>Ertalabki:</b> {weather_data['morning_temp']}°C ☀️
- <b>Kunduzgi:</b> {weather_data['afternoon_temp']}°C 🔆
- <b>Kechqurun:</b> {weather_data['evening_temp']}°C 🌙

☁️ <b>Ob-havo holati:</b> {weather_uzbek}

🌅 <b>Quyosh chiqishi:</b> {sunrise_time}
🌇 <b>Quyosh botishi:</b> {sunset_time}
"""
        return message


def get_currency_text():
    res1 = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
    data1 = res1.json()
    usd = data1[0]['Rate']
    euro = data1[1]['Rate']
    rub = data1[2]['Rate']
    currency_caption = f"""{formatted_date_uzbek} ҳолатига кўра валюта курслари:\n            
🇺🇸 Доллар курси: {usd} сўм
🇪🇺 Евро курси: {euro} сўм
🇷🇺 Рубл курси: {rub} сўм


    """
    return currency_caption


def send_message_akfa(caption, currency_caption):
    bot.send_photo("-1001583799449",
                   'https://i.pinimg.com/originals/6a/45/53/6a4553419e7852ebd3a5e253132ece18.jpg',
                   caption=caption,
                   parse_mode="HTML")
    bot.send_photo('-1001583799449',
                   'https://i.pinimg.com/originals/6a/45/53/6a4553419e7852ebd3a5e253132ece18.jpg',
                   caption=currency_caption,
                   parse_mode='HTML')


def send_message_pogodas(caption, currency_caption):
    bot2 = TeleBot(POGODAS_TOKEN, state_storage=StateMemoryStorage())
    bot2.send_photo("-1001215115441",
                    'http://itlink.uz/pogoda.jpeg',
                    caption=caption,
                    parse_mode="HTML")
    bot2.send_photo("-1001215115441",
                    'http://itlink.uz/currency.jpg',
                    caption=currency_caption,
                    parse_mode='HTML')


@bot.message_handler()
def get_info():
    res = requests.get('https://meteoapi.meteo.uz/api/weather/current')
    res1 = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
    data = res.json()
    tashkent = int(data[0]['air_t'])
    karakalpak = int(data[1]['air_t'])
    khorezm = int(data[2]['air_t'])
    bukhara = int(data[3]['air_t'])
    navai = int(data[4]['air_t'])
    samarkand = int(data[5]['air_t'])
    jizzakh = int(data[6]['air_t'])
    sirdarya = int(data[7]['air_t'])
    karshi = int(data[8]['air_t'])
    surkhandarya = int(data[9]['air_t'])
    fergana = int(data[10]['air_t'])
    namangan = int(data[11]['air_t'])
    andijan = int(data[12]['air_t'])
    tashkentregion = int(data[13]['air_t'])
    data1 = res1.json()
    usd = data1[0]['Rate']
    euro = data1[1]['Rate']
    rub = data1[2]['Rate']
    caption = f"""{formatted_date_uzbek} об-ҳаво маълумоти:\n
Тошкент ш. {tashkent} °C

Қорақалпоғистон {karakalpak} °C
Хоразм {khorezm} °C 

Бухоро {bukhara} °C 
Навоий {navai} °C 

Самарқанд {samarkand} °C 
Жиззах {jizzakh} °C 

Қашқадарё  {karshi} °C 
Сурхондарё  {surkhandarya} °C 

Сирдарё  {sirdarya} °C 
Тошкент в. {tashkentregion} °C 

Наманган  {namangan} °C
Андижон  {andijan} °C 
Фарғона {fergana} °C

"""
    currency_caption = f"""{formatted_date_uzbek} ҳолатига кўра валюта курслари:\n            
🇺🇸 Доллар курси: {usd} сўм
🇪🇺 Евро курси: {euro} сўм
🇷🇺 Рубл курси: {rub} сўм


"""
    #akfa_reklama = '<a href="https://www.instagram.com/akfa_build/">Instagram</a> | <a href="https://t.me/akfa_build_uz">Telegram</a> | <a href="https://akfabuild.com/">Website</a> | <a href="https://www.youtube.com/channel/UCp_5bF2PrOd5TwIKHSfkuXw">Youtube</a> | <a href="https://www.facebook.com/akfabuilduz">Facebook</a>'
    #try:
    #    send_message_akfa(caption + akfa_reklama, currency_caption + akfa_reklama)
    #except ApiTelegramException as e:
    #    logging.error(f"Channel Error: {str(e)}")
    pogodas_text_str = pogodas_text()
    print(pogodas_text_str)
    currency_text = get_currency_text()
    try:
        send_message_pogodas(pogodas_text_str, currency_text)
    except ApiTelegramException as e:
        logging.error(f"Channel Error: {str(e)}")


get_info()
