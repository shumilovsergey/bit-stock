from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import telegram_format
from server.const import TOKEN

@api_view(['POST'])
def getMessage(request):
    message = telegram_format(request.data)
    print(message)

    return Response("ok", status=200)
