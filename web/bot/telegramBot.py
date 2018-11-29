from django.core.handlers.wsgi import WSGIRequest
from .message import Message
import json
import requests
from django.db import models
from moneyCount.models import User, Category, Money

#todo Это выглядит как полное ублюдство 2.
# import sys
# import os
# sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))+'\\moneyCount\models')
# from models import User, Category, Money

# Метод getMessage получает сообщение в виде WSGIRequest
# Преобразует сообщение в объект класса Message
# Передает его в функцию parseMessage, где разбирает его и выполняет необходимые действия

class TelegramBot:
    class __TelegramBot:
        def __init__(self, token):
            self.token = token

    instance = None

    def __init__(self, token):
        if not TelegramBot.instance:
            TelegramBot.instance = TelegramBot.__TelegramBot(token)
        else:
            TelegramBot.instance.val = token
        self.token = token

    URL = 'https://api.telegram.org/bot'


    def parseMessage(self, msg: Message):
        print(msg)
        if (msg.text == '/start'):
            self.sendMessage(Message(msg.chatId, "Приветствую!\n"
                                                 "Данный бот создан для помощи в отслеживании ваших финансов.\n"
                                                 "Для получения справки по работе бота /help"))
        # Проверка на наличие пользователя в БД
        try:
            if (User.objects.get(chat_id__exact=msg.chatId)):
                pass
                # Основное тело выполнения, если пользователь в БД!
        except(Exception):
            print("User not in db!")
            # Добавить пользователя в БД


    def sendMessage(self, msg: Message):
        url = self.URL + self.token + '/sendmessage?chat_id={}&text={}'.format(msg.chatId, msg.text)
        requests.get(url)

    def getMessage(self, request: WSGIRequest):
        msg = Message()
        reqJson = json.loads(request.body)
        msg.text = reqJson["message"]["text"]
        msg.chatId = reqJson["message"]["chat"]["id"]
        self.parseMessage(msg)