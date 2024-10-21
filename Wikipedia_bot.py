import telebot
import wikipedia


TOKEN = '6574567041:AAHZH7RPYKbCTrY6ShTDIeyNaMqH9N_mQVk'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Сәлем, мен саған Уикипедиядан кез-келген ақпаратты жіберемін. Тек керек сөз немесе фразаңды жіберсең болғаны!")


@bot.message_handler(func=lambda message: True)
def send_info_from_wikipedia(message):
    try:
        
        wikipedia.set_lang("kk")
        search_result = wikipedia.summary(message.text)
        bot.reply_to(message, search_result)
    except wikipedia.exceptions.DisambiguationError as e:
        bot.reply_to(message, f"Сұранысыңды нақтыла. Мүмкін сен осыны меңзедің: {', '.join(e.options)}")
    except wikipedia.exceptions.PageError:
        # Егер ақпарат табылмаған жағдайда
        bot.reply_to(message, "Сен іздеген ақпарат табылмады.")
    except Exception as e:
        # Егер ақау пайда болғанда
        bot.reply_to(message, f"Техникалық ақау: {str(e)}")


bot.polling()
