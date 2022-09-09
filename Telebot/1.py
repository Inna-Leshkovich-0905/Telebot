#1922448950:AAEueQO_WmyT1wYrHbyaNV-FmeSirZ6zYy0

import telebot #подключение бота
from telebot import types #импорт библиотекм для создания кнопок в телеботе

token='1922448950:AAEueQO_WmyT1wYrHbyaNV-FmeSirZ6zYy0'
bot = telebot.TeleBot(token) #объявление бота


def create_keyboard(): #функция для создания кнопок
    keyboard = types.InlineKeyboardMarkup()
    drink_btn = types.InlineKeyboardButton(text="Хочу пить", callback_data='1')
    eat_btn = types.InlineKeyboardButton(text="Хочу есть", callback_data='2')
    keyboard.add(drink_btn) #выполнение функции
    keyboard.add(eat_btn)
    return keyboard #возврат

@bot.message_handler(commands=['start']) #чтобы функция срабатывала при команде бота "старт"
def start_bot(message): #функция, которая будет срабатывать при запуске
    keyboard=create_keyboard()
    bot.send_message(
        message.chat.id,
        "Добрый день! Выберите, что Вы хотите",
        reply_markup=keyboard #добавление кнопок keyboard
    )

@bot.callback_query_handler(func=lambda call:True) #добавление действий на кнопки
def callback_inline(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data=="1":
            img = open('9-17.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка воды",
                reply_markup=keyboard)
            img.close() #закрытие картинки
        if call.data == "2":
            img = open('darzoves2.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка еда",
                reply_markup=keyboard)
            img.close()


if __name__=="__main__": #запуск бота
    bot.polling(none_stop=True)