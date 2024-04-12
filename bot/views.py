from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import telegram_format
from api.models import TelegramUsers
from server.const import BACK_BUTTON
@api_view(['POST'])
def getMessage(request):
    message = telegram_format(request.data)
    print(message)

    if message.text and "/start" in message.text and len(message.text) > 8:
        signin(message)

    

    return Response("ok", status=200)

def signin(message):
    text=message.text
    session_id = text.replace("/start ", "")
    tg_id = message.chat_id

    # try:
    #     user = TelegramUsers.objects.get(tg_id=tg_id)
    #     user.session_id = session_id
    # except:
    user = TelegramUsers.objects.get(session_id=session_id)
    user.tg_id = tg_id

    user.save()
    
    message.sendMessage(text="http://bitstock.sh-development.ru/")

    return