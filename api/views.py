from django.views import View
from django.shortcuts import render, redirect
from .models import TelegramUsers
from .models import Orgs


class Main(View):
    def get(self, request):
        return render(request, 'main.html')
    
class Login(View):
    def get(self, request):
        session_id = request.session["session_id"]
        telegram_login_url = f"https://t.me/sh_login_testing_bot?start={session_id}"
        return redirect(telegram_login_url)
    
class Logout(View):
    def get(self, request):
        session_id = request.session["session_id"]
        if TelegramUsers.objects.filter(session_id=session_id).exists():
            user = TelegramUsers.objects.get(session_id=session_id)
            user.delete()
        request.session.clear()
        return redirect("/")
    
class Organisations(View):
    def get(self, request):
        session_id = request.session["session_id"]
        user = TelegramUsers.objects.get(session_id=session_id)
        orgs = Orgs.objects.filter(workers=user)
        return render(request, 'orgs.html', {"orgs":orgs})
    
    def post(self, request):
        org_name = request.POST["input_field"]
        session_id = request.session["session_id"]
        user = TelegramUsers.objects.get(session_id=session_id)
        org = Orgs.objects.create(boss_tg=user.tg_id, name=org_name)
        org.workers.add(user)
        return redirect("/orgs/")