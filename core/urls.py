from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('register/',views.register,name='register'),
    path('accounts/login/', views.user_login, name='login'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/',views.cart_view,name='cart'),
    path('increase/<int:item_id>/', views.increase_quantity),
    path('decrease/<int:item_id>/', views.decrease_quantity),
    path('remove/<int:item_id>/', views.remove_from_cart),
    path('profile/', views.profile, name='profile'),
]