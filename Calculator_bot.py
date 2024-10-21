import telebot


BOT_TOKEN = '7022951934:AAHyUET7CDBJXiNUaJJAMlt-7r_XLSyA46k'

bot = telebot.TeleBot(BOT_TOKEN)


first_number = None
operator = None

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Сәлем, мен калькулятор ботпын.")

@bot.message_handler(func=lambda message: message.text.isnumeric())
def handle_numbers(message):
    global first_number
    if first_number is None:
        first_number = float(message.text)
        bot.reply_to(message, "Өз сұранысыңды жібер")
    else:
        second_number = float(message.text)
        calculate()

@bot.message_handler(func=lambda message: message.text in ['+', '-', '*', '/'])
def handle_operators(message):
    global operator
    if first_number is None:
        bot.reply_to(message, "")
    else:
        operator = message.text

def calculate():
    global first_number, operator
    if operator == '+':
        result = first_number + second_number
    elif operator == '-':
        result = first_number - second_number
    elif operator == '*':
        result = first_number * second_number
    elif operator == '/':
        if second_number == 0:
            bot.reply_to(message, "0-ге бөлуге болмайды")
            return
        result = first_number / second_number
    else:
        bot.reply_to(message, "Қате!")
        return

    bot.reply_to(message, f"{first_number} {operator} {second_number} = {result}")
    first_number = None
    operator = None

@bot.message_handler(func=lambda message: True)
def handle_invalid(message):
    bot.reply_to(message, "Қате, осы операторларды қолданыңыз (+, -, *, /).")

if __name__ == '__main__':
    bot.polling()
