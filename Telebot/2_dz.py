#5576318822:AAFW1fP_E7QuUPmfv4ESdGo3uahRt-fFUCA

import telebot #подключение бота
from telebot import types #импорт библиотекм для создания кнопок в телеботе

token='5576318822:AAFW1fP_E7QuUPmfv4ESdGo3uahRt-fFUCA'
bot = telebot.TeleBot(token) #объявление бота

def create_keyboard(): #функция для создания кнопок
    keyboard = types.InlineKeyboardMarkup()
    soup_btn = types.InlineKeyboardButton(text="Хочу первое", callback_data='1')
    side_dich_btn = types.InlineKeyboardButton(text="Хочу второе", callback_data='2')
    dessert_btn = types.InlineKeyboardButton(text="Хочу десерт", callback_data='3')
    coffee_btn = types.InlineKeyboardButton(text="Хочу кофе", callback_data='4')
    tea_btn = types.InlineKeyboardButton(text="Хочу чай", callback_data='5')
    water_btn = types.InlineKeyboardButton(text="Хочу воды", callback_data='6')
    keyboard.add(soup_btn) #выполнение функции
    keyboard.add(side_dich_btn)
    keyboard.add(dessert_btn)
    keyboard.add(coffee_btn)
    keyboard.add(tea_btn)
    keyboard.add(water_btn)
    return keyboard #возврат

@bot.message_handler(commands=['start']) #чтобы функция срабатывала при команде бота "старт"
def start_bot(message): #функция, которая будет срабатывать при запуске
    keyboard=create_keyboard()
    bot.send_message(
        message.chat.id,
        "Здравствуйте! Выберите, пожалуйста, что Вы хотите:",
        reply_markup=keyboard #добавление кнопок keyboard
    )

@bot.callback_query_handler(func=lambda call:True) #добавление действий на кнопки
def callback_inline(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data=="1":
            img = open('Soup.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Приятного аппетита!",
                reply_markup=keyboard)
            img.close() #закрытие картинки
        if call.data=="2":
            img = open('Dish_second.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Приятного аппетита!",
                reply_markup=keyboard)
            img.close()
        if call.data=="3":
            img = open('Dessert.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Приятного аппетита!",
                reply_markup=keyboard)
            img.close()
        if call.data=="4":
            img = open('Coffee.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Приятного аппетита!",
                reply_markup=keyboard)
            img.close()
        if call.data=="5":
            img = open('Tea.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Приятного аппетита!",
                reply_markup=keyboard)
            img.close()
        if call.data=="6":
            img = open('Water.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Приятного аппетита!",
                reply_markup=keyboard)
            img.close()

if __name__=="__main__": #запуск бота
    bot.polling(none_stop=True)
