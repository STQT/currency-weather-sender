iconPhraseToUzbek = {
    "sunny": "Quyoshli",
    "mostly sunny": "Asosan Quyoshli",
    "partly sunny": "Qisman Quyoshli",
    "intermittent clouds": "Oralagan Bulutlar",
    "hazy sunshine": "Xaziy Quyosh",
    "mostly cloudy": "Asosan Bulutli",
    "cloudy": "Bulutli",
    "dreary (overcast)": "Qorong‘i (Bulutli)",
    "fog": "Tuman",
    "showers": "Yomg‘ir",
    "mostly cloudy w/ showers": "Asosan Bulutli va Yomg‘irli",
    "partly sunny w/ showers": "Qisman Quyoshli va Yomg‘irli",
    "t-storms": "To‘fonli",
    "mostly cloudy w/ t-storms": "Asosan Bulutli va To‘fonli",
    "partly sunny w/ t-storms": "Qisman Quyoshli va To‘fonli",
    "rain": "Yomg‘ir",
    "flurries": "Yengil Qor",
    "mostly cloudy w/ flurries": "Asosan Bulutli va Yengil Qorli",
    "partly sunny w/ flurries": "Qisman Quyoshli va Yengil Qorli",
    "snow": "Qor",
    "mostly cloudy w/ snow": "Asosan Bulutli va Qorli",
    "ice": "Muz",
    "sleet": "Yomg‘ir va Muz",
    "freezing rain": "Sovuq Yomg‘ir",
    "rain and snow": "Yomg‘ir va Qor",
    "hot": "Issiq",
    "cold": "Sovuq",
    "windy": "Shamolli",
    "clear": "Toza",
    "mostly clear": "Asosan Toza",
    "partly cloudy": "Qisman Bulutli",
    "hazy moonlight": "Xaziy Oy Nuri",
    "mostly cloudy": "Asosan Bulutli",
    "partly cloudy w/ showers": "Qisman Bulutli va Yomg‘irli",
    "mostly cloudy w/ showers": "Asosan Bulutli va Yomg‘irli",
    "partly cloudy w/ t-storms": "Qisman Bulutli va To‘fonli",
    "mostly cloudy w/ t-storms": "Asosan Bulutli va To‘fonli",
    "mostly cloudy w/ flurries": "Asosan Bulutli va Yengil Qorli",
    "mostly cloudy w/ snow": "Asosan Bulutli va Qorli",
}
def get_aqi_description(aqi_value):
    if aqi_value <= 50:
        return "Yaxshi",
    elif aqi_value <= 100:
        return "O'rtacha"
    elif aqi_value <= 150:
        return "Nozik guruhlar uchun nosog'lom"
    elif aqi_value <= 200:
        return "Nosog'lom"
    elif aqi_value <= 300:
        return "Juda nosog'lom"
    else:
        return "Xavfli"