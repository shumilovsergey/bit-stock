from django.shortcuts import redirect
import secrets
from .models import TelegramUsers

class CheckSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if "auth" not in request.session:
            print("mid-1")
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
            

        elif request.session["auth"] == False:
            session_id = request.session["session_id"]
            try:
                user = TelegramUsers.objects.get(session_id=session_id)
                if user.tg_id != "no-auth":
                    print("mid-2")
                    request.session["session_id"] = session_id
                    request.session["auth"] = True
                    request.session["name"] = user.name

            
            except:
                print("mid-3")
                request.session["auth"]=None
            #     print("mid-3")
            #     err = True
            #     session_id = secrets.token_hex(16)
            #     while err:
            #         try:
            #             TelegramUsers.objects.create(
            #                 session_id=session_id,
            #                 stocks_id={"id":"none"}
            #             )
            #             err=False
            #         except:
            #             session_id = secrets.token_hex(16) 

            #     request.session["session_id"] = session_id
            #     request.session["auth"] = False
            #     request.session["name"] = "no-auth"
        else:
            print("mid-4")    
            
        response = self.get_response(request)
        return response