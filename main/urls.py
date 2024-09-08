from django.urls import path
from main.views import show_main
from . import views

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('categories/', views.categories, name='categories'),
    path('products/', views.products, name='products'),
    path('cart/', views.cart, name='cart'),
]