from dotenv import load_dotenv
import os

load_dotenv()

# t.me/sh_login_testing_bot
TOKEN_TG = os.getenv("TOKEN_TG")

#back to webapp from bot
BACK_URL = "[вернуться на сайт](http://bitstock.sh-development.ru/)"


BACK_BUTTON= {
    "inline_keyboard" :  [
        [
            {'text': 'Вернуться на сайт', 'url': "https://bitstock.sh-development.ru/"}      
        ]
    ]
}

CLEAN_BUTTON= {
    "inline_keyboard" :  [
        [
            {'text': 'Вернуться на сайт', 'url': "https://bitstock.sh-development.ru/logout/"}      
        ]
    ]
}