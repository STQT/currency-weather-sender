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
    response = requests.get("https://media.leetcode.uz/info/aqi/?format=json")
    if response.status_code == 200:
        weather_data = response.json()
        message = f"""
🌤️ <b>Bugungi ob-havo</b>  
📍 <b>Shahar:</b> Toshkent  
📆 <b>Sana:</b> {datetime.strptime(weather_data['weather']['DailyForecasts'][0]['Date'], '%Y-%m-%dT%H:%M:%S%z').strftime('%d-%m-%Y')}  
        
🔆 <b>Kunduzgi ob-havo:</b>  
- <b>Harorat:</b> {weather_data['weather']['DailyForecasts'][0]['Temperature']['Maximum']['Value']}°C 
- <b>Havo:</b> {iconPhraseToUzbek[weather_data['weather']['DailyForecasts'][0]['Day']['IconPhrase']]} ☀️  
- <b>Shamol:</b> {weather_data['weather']['DailyForecasts'][0]['Day']['Wind']['Speed']['Value']} km/s  
- <b>Yomg'ir:</b> {weather_data['weather']['DailyForecasts'][0]['Day']['Rain']['Value']} mm 🌧️  
- <b>Qoplama:</b> {'Bulutsiz' if weather_data['weather']['DailyForecasts'][0]['Day']['CloudCover'] == 0 else 'Bulutli'} ☁️  
- <b>Nisbiy namlik:</b> {weather_data['weather']['DailyForecasts'][0]['Day']['RelativeHumidity']['Average']}%  

🌙 <b>Tungi ob-havo:</b>  
- <b>Harorat:</b> {weather_data['weather']['DailyForecasts'][0]['Temperature']['Minimum']['Value']}°C
- <b>Havo:</b> {iconPhraseToUzbek[weather_data['weather']['DailyForecasts'][0]['Night']['IconPhrase']]} 🌙  
- <b>Shamol:</b> {weather_data['weather']['DailyForecasts'][0]['Night']['Wind']['Speed']['Value']} km/s  
- <b>Yomg'ir:</b> {weather_data['weather']['DailyForecasts'][0]['Night']['Rain']['Value']} mm 🌧️  

⚠️ <b>Havo sifati:</b>  
- <b>Ozon:</b> {next((item['Value'] for item in weather_data['weather']['DailyForecasts'][0]['AirAndPollen'] if item['Name'] == 'AirQuality'), 'N/A')} 🌿  
- <b>UV ko'rsatkichi:</b> {next((item['Value'] for item in weather_data['weather']['DailyForecasts'][0]['AirAndPollen'] if item['Name'] == 'UVIndex'), 'N/A')} ☀️ 
- <b>Iflosligi:</b> {weather_data['aqi']['data']['current']['pollution']['aqius']}
- <b>Inson sog'lig'iga ta'siri:</b> {get_aqi_description(weather_data['aqi']['data']['current']['pollution']['aqius'])[0]}
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
    bot2.send_photo(390736292,
                    'http://itlink.uz/pogoda.jpeg',
                    caption=caption,
                    parse_mode="HTML")
    bot2.send_photo(390736292,
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
    akfa_reklama = '<a href="https://www.instagram.com/akfa_build/">Instagram</a> | <a href="https://t.me/akfa_build_uz">Telegram</a> | <a href="https://akfabuild.com/">Website</a> | <a href="https://www.youtube.com/channel/UCp_5bF2PrOd5TwIKHSfkuXw">Youtube</a> | <a href="https://www.facebook.com/akfabuilduz">Facebook</a>'
    try:
        send_message_akfa(caption + akfa_reklama, currency_caption + akfa_reklama)
    except ApiTelegramException as e:
        logging.error(f"Channel Error: {str(e)}")
    try:
        send_message_pogodas(pogodas_text(), get_currency_text())
    except ApiTelegramException as e:
        logging.error(f"Channel Error: {str(e)}")


get_info()
