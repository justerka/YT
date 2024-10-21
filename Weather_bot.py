import json
import telebot
import requests

bot = telebot.TeleBot('6999606865:AAG9cOcUDxHEu98zPwxuPFzdakX42_RpPnk')
API = '18fba8fe4f1847d53b79539c612a59fa'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id , 'Сәлем, өзіңнің қалаңды ағылшынша жаз')

@bot.message_handler(content_types=['text'])
def weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(res.text)
    bot.reply_to(message, f'Қазір ауа райы: {data['main']['temp']}')
bot.polling(none_stop=True)
