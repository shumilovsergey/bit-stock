from django.contrib import admin
from .models import TelegramUsers
from .models import Orgs
from .models import Products
from .models import Categories

admin.site.register(TelegramUsers)
admin.site.register(Orgs)
admin.site.register(Products)
admin.site.register(Categories)
