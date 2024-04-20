from django.contrib import admin
from .models import TelegramUsers
from .models import Orgs

admin.site.register(TelegramUsers)
admin.site.register(Orgs)
