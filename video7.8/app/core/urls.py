from django.urls import path
from core.views.category.views import *


app_name = 'erp'

#urlpatterns = [
#    path('category/list/', CategoryListView.as_view(), name='vista1'),
#    path('category/list2/', category_list, name='vista2'),
#]

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/list2/', category_list, name='category_list2'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),

]