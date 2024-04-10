from django.urls import path
from .views import Main
from .views import Login

app_name = 'api'
urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('login/', Login.as_view(), name='login'),
]