import telebot

bot = telebot.TeleBot('6712909162:AAHQgSsYWiIz0WJ4UUfT6bLM56gr6btrMEU')


@bot.message_handler(commands=['start'])
def main(messange):
    bot.send_message(messange.chat.id, 'Привет!')


@bot.message_handler(commands=['support'])
def main(messange):
    bot.send_message(messange.chat.id,
                      'Ты обязательно справишься и пройдешь через все это. Тебе очень тяжело, но крепись.')


@bot.message_handler(commands=['love'])
def main(messange):
    bot.send_message(messange.chat.id, 'Ты прелесть!')


@bot.message_handler(commands=['sad'])
def main(messange):
    bot.send_message(messange.chat.id, '[Подними себе настроение](https://youtu.be/Kd01GtuwnP8?si=50CDXbqSVUx96uQj)',
                      parse_mode='Markdown')


bot.infinity_polling()