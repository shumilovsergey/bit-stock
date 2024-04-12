from django.views import View
from django.shortcuts import render, redirect
from .models import TelegramUsers

import secrets

class Main(View):
    def get(self, request):

        return render(request, 'index.html')
    

class Login(View):
    def get(self, request):
        
        return render(request, 'login.html', {"telegram_login_url":"/sign/"})
    

class Sign(View):
    def get(self, request):
        err = True
        session_id = secrets.token_hex(16) 

        while err:
            try:
                TelegramUsers.objects.create(
                    session_id=session_id,
                    stocks_id={"id":"none"}
                )
                err=False
            except:
                session_id = secrets.token_hex(16) 

        request.session['session_id'] = session_id
        telegram_login_url = f"https://t.me/sh_login_testing_bot?start={session_id}"
        return redirect(telegram_login_url)