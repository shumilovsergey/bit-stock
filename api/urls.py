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
from .views import Organisation_Select

from .views import Worker_List
from .views import Worker_Delete

from .views import Category_List
from .views import Category_Add
from .views import Category_Delete

from .views import Product_Page
from .views import Product_Delete
from .views import Product_Edit
from .views import Product_List
from .views import Product_Add

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
    path('org_page/select/<int:org_id>', Organisation_Select.as_view(), name='org_select'),

    path('worker_list', Worker_List.as_view(), name='worker_list'),
    path('worker_delete/<int:worker_tg>', Worker_Delete.as_view(), name='worker_delete'),

    path('category_list/', Category_List.as_view(), name='category_list'),
    path('category_add/', Category_Add.as_view(), name='category_add'),
    path('category_delete/<int:category_id>', Category_Delete.as_view(), name='category_delete'),

    path('product_list/', Product_List.as_view(), name='product_list'),      
    path('product/<int:product_id>', Product_Page.as_view(), name='product_page'),
    path('product/delete/<int:product_id>', Product_Delete.as_view(), name='product_delete'),
    path('product/edit/<int:product_id>', Product_Edit.as_view(), name='product_edit'),
    path('product/add/', Product_Add.as_view(), name='product_add'),
]


