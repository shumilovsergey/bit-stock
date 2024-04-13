from django.views import View
from django.shortcuts import render, redirect
from .models import TelegramUsers


class Main(View):
    def get(self, request):
        print(request.session["session_id"])
        print(request.session["auth"])

        return render(request, 'main.html', {
            "telegram_login_url":"/login/",
            "telegram_logout_url":"/logout/",
        })
    
class Login(View):
    def get(self, request):
        session_id = request.session["session_id"]
        telegram_login_url = f"https://t.me/sh_login_testing_bot?start={session_id}"
        print(telegram_login_url)
        return redirect(telegram_login_url)
    
class Logout(View):
    def get(self, request):
        session_id = request.session["session_id"]
        user = TelegramUsers.objects.get(session_id=session_id)
        user.delete()
        del request.session["auth"]
        return redirect("/")