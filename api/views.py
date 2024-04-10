from django.views import View
from django.shortcuts import render

class Main(View):
    def get(self, request):
        return render(request, 'index.html')
    
class Login(View):
    def get(self, request):
        token= 0
        print(type(request))

        telegram_login_url = f"https://t.me/wget_bash_bot?start={token}"
        return render(request, 'login.html', {"telegram_login_url":telegram_login_url})
    

# Model 
