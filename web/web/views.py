from django.http import HttpResponse, JsonResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

#todo Это выглядит как полное ублюдство.
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))+'\\bot')

from bot.telegramBot import TelegramBot


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def json(request):
    return JsonResponse({'test': 'test'})

@csrf_exempt
def bot(request):

    tlgBot = TelegramBot("710654947:AAH57NV4Q8hfSyKtubOBYx44WbhHjQcD5ws")
    tlgBot.getMessage(request)
    return HttpResponse("Nice work, man!")