from django.views import View
from django.shortcuts import render, redirect
from .models import TelegramUsers
from .models import Orgs
from .models import Categories
from .models import Products

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
        request.session["org_select"]=None
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
            info = "У вас нет прав на удаление"
            return render(request, 'info.html', {"info":info}) 
        
        org.delete()
        request.session["org_select"]=None
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
    
class Organisation_Select(View):
    def get(self, request, org_id):
        session_id = request.session["session_id"]
        user = TelegramUsers.objects.get(session_id=session_id)
        org = Orgs.objects.get(id=org_id)
        if not org.workers.filter(session_id=session_id).exists():
            info = "Вы не состоите в этой организации"
            return render(request, 'info.html', {"info":info})
        
        request.session["org_select"]=org.id
        return redirect('api:org_list')

class Worker_List(View):
    def get(self, request):
        org_id = request.session["org_select"]
        session_id = request.session["session_id"]
        user = TelegramUsers.objects.get(session_id=session_id)

        if not Orgs.objects.filter(id=org_id).exists():
            info = "Нет такой организации"
            return render(request, 'info.html', {"info":info})
        
        org = Orgs.objects.get(id=org_id)
        if not org.workers.filter(session_id=session_id).exists():
            info = "Вы не состоите в этой организации"
            return render(request, 'info.html', {"info":info})
        
        workers = org.workers.all()
        return render(request, 'worker_list.html', {"workers":workers})

class Worker_Delete(View):
    def post(self, request, worker_tg):
        org_id = request.session["org_select"]
        session_id = request.session["session_id"]
        user = TelegramUsers.objects.get(session_id=session_id)

        if not Orgs.objects.filter(id=org_id).exists():
            info = "Нет такой организации"
            return render(request, 'info.html', {"info":info})
        
        org = Orgs.objects.get(id=org_id)
        if user.tg_id != org.boss_tg:
            info = "У вас нет прав на увольнение"
            return render(request, 'info.html', {"info":info}) 
        
        if user.tg_id == str(worker_tg):
            info = "Нельзя уволить начальника организации!"
            return render(request, 'info.html', {"info":info})
        
        worker = TelegramUsers.objects.get(tg_id=worker_tg)
        org.workers.remove(worker)
        org.save()
        return redirect('api:worker_list')
    
class Category_List(View):
    def get(self, request):
        org_id = request.session["org_select"]
        session_id = request.session["session_id"]

        if not Orgs.objects.filter(id=org_id).exists():
            info = "Нет такой организации"
            return render(request, 'info.html', {"info":info})
        
        org = Orgs.objects.get(id=org_id)
        if not org.workers.filter(session_id=session_id).exists():
            info = "Вы не состоите в этой организации"
            return render(request, 'info.html', {"info":info})
        
        categories = Categories.objects.filter(org=org)
        return render(request, 'category_list.html', {"categories":categories})
    
class Category_Add(View):
    def post(self, request):
        category_name = request.POST["input_field"]
        org_id = request.session["org_select"]
        session_id = request.session["session_id"]

        if not Orgs.objects.filter(id=org_id).exists():
            info = "Нет такой организации"
            return render(request, 'info.html', {"info":info})
        
        org = Orgs.objects.get(id=org_id)
        if not org.workers.filter(session_id=session_id).exists():
            info = "Вы не состоите в этой организации"
            return render(request, 'info.html', {"info":info})

        category_list = Categories.objects.filter(org=org_id)
        for c in category_list:
            if category_name.lower() == c.name.lower():
                info = "У вас уже есть такая категория"
                return render(request, 'info.html', {"info":info})

        Categories.objects.create(name=category_name, org=org)    
        return redirect('api:category_list')

class Category_Delete(View):
    def post(self, request, category_id):
        org_id = request.session["org_select"]
        session_id = request.session["session_id"]
        user = TelegramUsers.objects.get(session_id=session_id)

        if not Orgs.objects.filter(id=org_id).exists():
            info = "Нет такой организации"
            return render(request, 'info.html', {"info":info})
        
        org = Orgs.objects.get(id=org_id)
        if not org.workers.filter(session_id=session_id).exists():
            info = "Вы не состоите в этой организации"
            return render(request, 'info.html', {"info":info})
        
        if user.tg_id != org.boss_tg:
            info = "У вас нет прав на удаление категорий!"
            return render(request, 'info.html', {"info":info}) 

        if not Categories.objects.filter(id=category_id).exists():
            info = "Нет такой категории"
            return render(request, 'info.html', {"info":info})
        
        category = Categories.objects.get(id=category_id)
        category.delete()
        return redirect('api:category_list')

class Product_List(View):
    def get(self, request):
        org_id = request.session["org_select"]
        session_id = request.session["session_id"]

        if not Orgs.objects.filter(id=org_id).exists():
            info = "Нет такой организации"
            return render(request, 'info.html', {"info":info})
        
        org = Orgs.objects.get(id=org_id)
        if not org.workers.filter(session_id=session_id).exists():
            info = "Вы не состоите в этой организации"
            return render(request, 'info.html', {"info":info})
        
        products = Products.objects.filter(org=org).select_related('category', 'org').order_by('category__name')

        categories = {}
        for product in products:
            if product.category.name not in categories:
                categories[product.category.name] = []
            categories[product.category.name].append(product)

        return render(request, 'product_list.html', {"categories":categories})

class Product_Page(View):
    def get(self, request, product_id):
        org_id = request.session["org_select"]
        session_id = request.session["session_id"]

        if not Orgs.objects.filter(id=org_id).exists():
            info = "Нет такой организации"
            return render(request, 'info.html', {"info":info})
        
        org = Orgs.objects.get(id=org_id)
        if not org.workers.filter(session_id=session_id).exists():
            info = "Вы не состоите в этой организации"
            return render(request, 'info.html', {"info":info})

        if not Products.objects.filter(id=product_id).exists():
            info = "Нет такого продукта!"
            return render(request, 'info.html', {"info":info})
        
        product=Products.objects.get(id=product_id)
        category_list = Categories.objects.filter(org=org_id)
        return render(request, 'product_page.html', {"category_list":category_list, "product":product})
    
class Product_Delete(View):
    def post(self, request, product_id):
        org_id = request.session["org_select"]
        session_id = request.session["session_id"]

        if not Orgs.objects.filter(id=org_id).exists():
            info = "Нет такой организации"
            return render(request, 'info.html', {"info":info})
        
        org = Orgs.objects.get(id=org_id)
        if not org.workers.filter(session_id=session_id).exists():
            info = "Вы не состоите в этой организации"
            return render(request, 'info.html', {"info":info})

        if not Products.objects.filter(id=product_id).exists():
            info = "Нет такого продукта!"
            return render(request, 'info.html', {"info":info})
        
        user = TelegramUsers.objects.get(session_id=session_id)
        if user.tg_id != org.boss_tg:
            info = "У вас нет прав на удаление карточки товара"
            return render(request, 'info.html', {"info":info}) 
        
        product = Products.objects.get(id=product_id)
        product.delete()
        return redirect('api:product_list')
    
class Product_Edit(View):
    def post(self, request, product_id):
        org_id = request.session["org_select"]
        session_id = request.session["session_id"]

        if not Orgs.objects.filter(id=org_id).exists():
            info = "Нет такой организации"
            return render(request, 'info.html', {"info":info})
        
        org = Orgs.objects.get(id=org_id)
        if not org.workers.filter(session_id=session_id).exists():
            info = "Вы не состоите в этой организации"
            return render(request, 'info.html', {"info":info})

        if not Products.objects.filter(id=product_id).exists():
            info = "Нет такого продукта!"
            return render(request, 'info.html', {"info":info})
        
        product = Products.objects.get(id=product_id)
        if product.count != request.POST["count"]:
            info = "Сотрудник может менять количество товаров только через сделки!"
            return render(request, 'info.html', {"info":info})
        
        try:
            product.name=request.POST["name"]
            product.description=request.POST["description"]
            category = Categories.objects.get(id=int(request.POST["category"]))
            product.category=category
            product.count=request.POST["count"]
            product.save()
            return redirect('api:product_list')
        
        except:
            info = "Ошибка записи"
            return render(request, 'info.html', {"info":info})
        
    
class Product_Add(View):
    def get(self, request):
        org_id = request.session["org_select"]
        session_id = request.session["session_id"]

        if not Orgs.objects.filter(id=org_id).exists():
            info = "Нет такой организации"
            return render(request, 'info.html', {"info":info})
        
        org = Orgs.objects.get(id=org_id)
        if not org.workers.filter(session_id=session_id).exists():
            info = "Вы не состоите в этой организации"
            return render(request, 'info.html', {"info":info})
        
        category_list = Categories.objects.filter(org=org_id)
        return render(request, 'product_add.html', {"category_list":category_list})

    def post(self, request):
        org_id = request.session["org_select"]
        session_id = request.session["session_id"]

        if not Orgs.objects.filter(id=org_id).exists():
            info = "Нет такой организации"
            return render(request, 'info.html', {"info":info})
        
        org = Orgs.objects.get(id=org_id)
        if not org.workers.filter(session_id=session_id).exists():
            info = "Вы не состоите в этой организации"
            return render(request, 'info.html', {"info":info})
        
        try:
            category = Categories.objects.get(id=int(request.POST["category"]))
            Products.objects.create(
                name=request.POST["name"],
                description=request.POST["description"],
                category=category,
                count=0,
                org=org
            )

            return redirect('api:product_list')
        
        except:
            info = "Ошибка записи"
            return render(request, 'info.html', {"info":info})
        

