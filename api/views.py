from django.views import View
from django.shortcuts import render
from rest_framework.authtoken.models import Token

class Main(View):
    def get(self, request):
        # token = request.session.get('token')
        # print(token)
        return render(request, 'index.html')
    




class Login(View):
    def get(self, request):
        

        token= "token exaple code 2"
        request.session['token'] = token

        telegram_login_url = f"https://t.me/wget_bash_bot?start={token}"
        return render(request, 'login.html', {"telegram_login_url":telegram_login_url})
    

# Model 
