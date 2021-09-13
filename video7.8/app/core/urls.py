from django.urls import path
from core.views.category.views import *


app_name = 'erp'

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='vista1'),
    #path('category/list2/', category_list, name='vista2'),
]