from django.urls import path
from . import views


app_name = 'product'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>', views.product_list, name='product_list_category'),
    path('details/<slug:product_slug>', views.product_details, name='product_details'),

]
