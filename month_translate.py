from datetime import datetime


month_translation = {
    "January": "Январь",
    "February": "Февраль",
    "March": "Март",
    "April": "Апрель",
    "May": "Май",
    "June": "Июнь",
    "July": "Июль",
    "August": "Август",
    "September": "Сентябрь",
    "October": "Октябрь",
    "November": "Ноябрь",
    "December": "Декабрь"
}

current_date = datetime.now()

formatted_date_english = current_date.strftime("%d %B")

english_month_name = formatted_date_english.split()[1]


uzbek_cyrilic_month = month_translation.get(english_month_name,english_month_name)

formatted_date_uzbek = f"{current_date.strftime('%d')} {uzbek_cyrilic_month}"


