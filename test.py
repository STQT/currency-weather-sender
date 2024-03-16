import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['get_channel_id'])
def get_channel_id(message):
    sent_message = bot.get_chat('@akfa_build_uz')
    channel_id = sent_message.id
    bot.reply_to(message, f"The ID of the channel is: {channel_id}")


bot.polling()
