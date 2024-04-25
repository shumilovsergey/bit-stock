from django.urls import path
from .views import Main
from .views import Login
from .views import Logout
from .views import Organisation_List
from .views import Organisation_Page
from .views import Organisation_Edit
from .views import Organisation_Delete
from .views import Organisation_Create
from .views import Organisation_Invite


app_name = 'api'
urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('org_list/', Organisation_List.as_view(), name='org_list'),
    path('org_page/<int:org_id>/', Organisation_Page.as_view(), name='org_page'),
    path('org_page/edit/<int:org_id>/', Organisation_Edit.as_view(), name='org_edit'),
    path('org_page/delete/<int:org_id>/', Organisation_Delete.as_view(), name='org_delete'),
    path('org_page/create/', Organisation_Create.as_view(), name='org_create'),
    path('org_page/invite/<int:org_id>', Organisation_Invite.as_view(), name='org_invite'),
]