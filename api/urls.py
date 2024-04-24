from django.urls import path
from .views import Main
from .views import Login
from .views import Logout
from .views import Organisation_list
from .views import Organisation
from .views import OrganisationDelete


app_name = 'api'
urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('org_list/', Organisation_list.as_view(), name='org_list'),
    path('org/', Organisation.as_view(), name='org'),
    path('org/delete/<int:org_id>', OrganisationDelete.as_view(), name='org_del')
]