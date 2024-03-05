#1
# from collections import namedtuple
#
# Book = namedtuple('Book','title author janr year')
#
# books = [ ( 'O\'tgan kunlar','Abdulla Qodirov','Ishqiy','1992' ),
#           ('Shaytanat','O\'tkir Hoshimov','Jangari','1995'),
#           ('Yuksak ma\'naviyat yengilmas kuch','Islom Kaimov','Siyosiy','2012')     ]
#
# for book in books:
#     book1 = Book(*book)
# print(book1.author, book1.year)
# -----------------------------------------------------------------------------------
#2 Telegrambot
# from telebot import TeleBot
# from telebot.types import Message
# bot = TeleBot('7106668865:AAGb7YhiIZcG7nV5xaawapJNKy7nkJGjEk0')
#
# @bot.message_handler(commands=['start'])
# def start(message:Message):
#     chat_id = message.chat.id
#     first_name = message.from_user.first_name
#     print(chat_id)
#     bot.send_message(chat_id=chat_id, text=f"Assalomu aleykum {first_name}")
#
# @bot.message_handler(content_types=['text','photo','video','animation'])
# def return_to_text(message:Message):
#     chat_id = message.chat.id
#     bot.copy_message(-1002118445907, chat_id,message.message_id)
#
#
# bot.polling()