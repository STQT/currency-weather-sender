iconPhraseToUzbek = {
    "Sunny": "Quyoshli",
    "Mostly Sunny": "Asosan Quyoshli",
    "Partly Sunny": "Qisman Quyoshli",
    "Intermittent Clouds": "Oralagan Bulutlar",
    "Hazy Sunshine": "Xaziy Quyosh",
    "Mostly Cloudy": "Asosan Bulutli",
    "Cloudy": "Bulutli",
    "Dreary (Overcast)": "Qorong‘i (Bulutli)",
    "Fog": "Tuman",
    "Showers": "Yomg‘ir",
    "Mostly Cloudy w/ Showers": "Asosan Bulutli va Yomg‘irli",
    "Partly Sunny w/ Showers": "Qisman Quyoshli va Yomg‘irli",
    "T-Storms": "To‘fonli",
    "Mostly Cloudy w/ T-Storms": "Asosan Bulutli va To‘fonli",
    "Partly Sunny w/ T-Storms": "Qisman Quyoshli va To‘fonli",
    "Rain": "Yomg‘ir",
    "Flurries": "Yengil Qor",
    "Mostly Cloudy w/ Flurries": "Asosan Bulutli va Yengil Qorli",
    "Partly Sunny w/ Flurries": "Qisman Quyoshli va Yengil Qorli",
    "Snow": "Qor",
    "Mostly Cloudy w/ Snow": "Asosan Bulutli va Qorli",
    "Ice": "Muz",
    "Sleet": "Yomg‘ir va Muz",
    "Freezing Rain": "Sovuq Yomg‘ir",
    "Rain and Snow": "Yomg‘ir va Qor",
    "Hot": "Issiq",
    "Cold": "Sovuq",
    "Windy": "Shamolli",
    "Clear": "Toza",
    "Mostly Clear": "Asosan Toza",
    "Partly Cloudy": "Qisman Bulutli",
    "Hazy Moonlight": "Xaziy Oy Nuri",
    "Mostly Cloudy": "Asosan Bulutli",
    "Partly Cloudy w/ Showers": "Qisman Bulutli va Yomg‘irli",
    "Mostly Cloudy w/ Showers": "Asosan Bulutli va Yomg‘irli",
    "Partly Cloudy w/ T-Storms": "Qisman Bulutli va To‘fonli",
    "Mostly Cloudy w/ T-Storms": "Asosan Bulutli va To‘fonli",
    "Mostly Cloudy w/ Flurries": "Asosan Bulutli va Yengil Qorli",
    "Mostly Cloudy w/ Snow": "Asosan Bulutli va Qorli",
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