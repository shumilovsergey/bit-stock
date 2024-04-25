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
            user.session_id = "None"
            user.save()

        request.session["session_id"]=None
        request.session["auth"]=None
        request.session["name"]=None
        return redirect("/")
    
class Organisation_List(View):
    def get(self, request):
        session_id = request.session["session_id"]
        user = TelegramUsers.objects.get(session_id=session_id)
        orgs = Orgs.objects.filter(workers=user)
        return render(request, 'org_list.html', {"orgs":orgs})
       
class Organisation_Page(View):
    def get(self, request, org_id):
        session_id = request.session["session_id"]
        user = TelegramUsers.objects.get(session_id=session_id)

        if not Orgs.objects.filter(id=org_id).exists():
            info = "Нет такой организации"
            return render(request, 'info.html', {"info":info})

        org = Orgs.objects.get(id=org_id)
        if not org.workers.filter(session_id=session_id).exists():
            info = "Вы не состоите в этой организации"
            return render(request, 'info.html', {"info":info})
        
        return render(request, "org_page.html", {"org":org})


class Organisation_Edit(View):
    def post(self, request, org_id):
        name = request.POST["input_field"]
        session_id = request.session["session_id"]
        user = TelegramUsers.objects.get(session_id=session_id)

        if not Orgs.objects.filter(id=org_id).exists():
            info = "Нет такой организации"
            return render(request, 'info.html', {"info":info})

        org = Orgs.objects.get(id=org_id)
        if user.tg_id != org.boss_tg:
            info = "У вас нет прав не смену названия"
            return render(request, 'info.html', {"info":info}) 
        
        org.name=name
        org.save()
        return redirect('api:org_list')
    
class Organisation_Delete(View):
    def post(self, request, org_id):
        session_id = request.session["session_id"]
        user = TelegramUsers.objects.get(session_id=session_id)

        if not Orgs.objects.filter(id=org_id).exists():
            info = "Нет такой организации"
            return render(request, 'info.html', {"info":info})

        org = Orgs.objects.get(id=org_id)
        if user.tg_id != org.boss_tg:
            info = "У вас нет прав не смену названия"
            return render(request, 'info.html', {"info":info}) 
        
        org.delete()
        return redirect('api:org_list')
    
class Organisation_Create(View):
    def post(self, request):
        session_id = request.session["session_id"]
        user = TelegramUsers.objects.get(session_id=session_id)
        name = request.POST["input_field"]

        org=Orgs.objects.create(name=name, boss_tg=user.tg_id)
        org.workers.add(user)
        org.save()
        return redirect('api:org_list')
    
class Organisation_Invite(View):
    def get(self, request, org_id):
        session_id = request.session["session_id"]
        user = TelegramUsers.objects.get(session_id=session_id)

        if not Orgs.objects.filter(id=org_id).exists():
            info = "Нет такой организации"
            return render(request, 'info.html', {"info":info})
        
        org = Orgs.objects.get(id=org_id)
        if org.workers.filter(id=user.id).exists():
            info = "Вы уже состоите в этой организации"
            return render(request, 'info.html', {"info":info})
        
        org.workers.add(user)
        return redirect('api:org_list')