# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Application, MessageHandler, filters, CommandHandler, CallbackQueryHandler
# from telegram import ForceReply
#
# API_KEY = '7553875249:AAGUo2VpsaaUHnKhkYianL6cnYVyV1EAwK0'
#
#
# # async def echo(update: Update, context) -> None:
# #     """Отправка ответа с тем же текстом."""
# #     user_message = update.message.text
# #     await update.message.reply_text(user_message)
# #
# #
# # async def start(update: Update, context) -> None:
# #     """Отправка приветственного сообщения."""
# #     user = update.effective_user
# #     await update.message.reply_html(
# #         rf"Hi {user.mention_html()}! Welcome to the bot.",
# #         reply_markup=ForceReply(selective=True),
# #     )
# #
# #
# # async def help_command(update: Update, context) -> None:
# #     """Отправка помощи по боту."""
# #     await update.message.reply_text("Use /start to get started.")
#
#
# async def start(update: Update, context) -> None:
#     """Отправка сообщения с кнопкой."""
#     keyboard = [
#         [InlineKeyboardButton("Click Me 1", callback_data='button_click_1')],
#         [InlineKeyboardButton("Click Me 2", callback_data='button_click_2')],
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await update.message.reply_text('Hello! Press the button below:', reply_markup=reply_markup)
#
#
# async def button(update: Update, context) -> None:
#     """Обработка нажатия на кнопку."""
#     query = update.callback_query
#     await query.answer()
#     await query.edit_message_text(text="You clicked the button! {}".format(query.data))
#
#
# # Create the Application and pass it your bot's token.
# application = Application.builder().token(API_KEY).build()
#
# # application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
# # application.add_handler(CommandHandler('start', start))
# # application.add_handler(CommandHandler('help', help_command))
#
# application.add_handler(CommandHandler("start", start))
# application.add_handler(CallbackQueryHandler(button, pattern="^button_click"))
#
# # Run the bot until the user presses Ctrl-C
# application.run_polling(allowed_updates=Update.ALL_TYPES)






import telebot
from telebot import types

API_KEY = '7553875249:AAGUo2VpsaaUHnKhkYianL6cnYVyV1EAwK0'
bot = telebot.TeleBot(API_KEY)

user_state = {}

# @bot.message_handler(commands=['photo'])
# def send_photo(message):
#
#     with open('photo_2024-12-16_11-35-41.jpg', 'rb') as photo_file:
#         bot.send_document(message.chat.id, photo_file, caption="Here is a nice photo!")

@bot.message_handler(commands=['location'])
def send_location(message):
    latitude = 51.5074
    longitude = 0.1278
    bot.send_location(message.chat.id, latitude, longitude)


# @bot.message_handler(commands=['start'])
# def start(message):
#     user_state[message.chat.id] = 'CHOICE'
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.row('Option 1', 'Option 2')
#     bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)
#
#
# @bot.message_handler(func=lambda message: user_state.get(message.chat.id) == 'CHOICE')
# def choice(message):
#     if message.text == 'Option 1':
#         user_state[message.chat.id] = 'NAME'
#         bot.send_message(message.chat.id, "What's your name?")
#     elif message.text == 'Option 2':
#         user_state[message.chat.id] = 'AGE'
#         bot.send_message(message.chat.id, "How old are you?")
#
#
# @bot.message_handler(func=lambda message: user_state.get(message.chat.id) == 'NAME')
# def name(message):
#     user_state[message.chat.id] = 'Q1'
#     bot.send_message(message.chat.id, f"Your name is {message.text}. How old are you?")
#
#
# @bot.message_handler(func=lambda message: user_state.get(message.chat.id) == 'Q1')
# def q1(message):
#     user_state[message.chat.id] = 'AGE'
#     bot.send_message(message.chat.id, f"Q1")
#
#
# @bot.message_handler(func=lambda message: user_state.get(message.chat.id) == 'AGE')
# def age(message):
#     bot.send_message(message.chat.id, f"You're {message.text} years old. Thanks for the info!")
#     del user_state[message.chat.id]



bot.polling()
