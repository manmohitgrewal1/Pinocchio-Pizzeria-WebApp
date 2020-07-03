from django.urls import path
import re
from . import views as user_views
from django.contrib.auth import views as auth_views
app_name='orders'
urlpatterns = [
    path("", user_views.index, name="index"),
    path("cart/", user_views.cart, name='cart'),
    path("register/", user_views.register, name='register'),
    path("login/", auth_views.LoginView.as_view(template_name='orders/login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='orders/logout.html'), name='logout'),
    path("selectMode/<str:detail>/", user_views.index, name= "index")
    
]
