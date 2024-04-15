from django.shortcuts import redirect
import secrets
from .models import TelegramUsers
from django.utils import timezone

class CheckSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if "bot" in request.path:
            print("")
            print("SessionMiddll ignore /bot")
            print("")
            response = self.get_response(request)
            return response

        if "auth" not in request.session:
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

            request.session["session_id"] = session_id
            request.session["auth"] = False
            request.session["name"] = "no-auth"
            #dell all session no-auth older 1 day
            cutoff_date = timezone.now() - timezone.timedelta(days=1)
            TelegramUsers.objects.filter(created=cutoff_date, tg_id="no-auth").delete()
            

        elif request.session["auth"] == False:
            session_id = request.session["session_id"]
            try:
                user = TelegramUsers.objects.get(session_id=session_id)
                if user.tg_id != "no-auth":
                    request.session["session_id"] = session_id
                    request.session["auth"] = True
                    request.session["name"] = user.name

            except:
                print("mid-3")
                request.session["auth"]=None

        response = self.get_response(request)
        return response
    

class SessionDebuger:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if "bot" in request.path:
            print("")
            print("SessionDebbugerMidd ignore /bot")
            print("")
            response = self.get_response(request)
            return response
        
        auth = request.session["auth"]
        session_id = request.session["session_id"]
        user = request.session["name"] 


        print("##_______SESSION____##")
        print(f"auth status - {auth}")
        print(f"session_id  - {session_id}")
        print(f"user name   - {user}")
        print(" ")
        print(" ")

        path_exceptions = [
            "/",
            "/bot",
            "/login/",
            "/logout/"
        ]

        # if "/admin" not in request.path and request.path != "/" and request.path != "/login/":
        if "/admin" not in request.path and request.path not in path_exceptions:
            print(" ")
            print(f"SessionDebugerMidd redirect {request.path} to the /")
            return redirect("/")

        response = self.get_response(request)
        return response