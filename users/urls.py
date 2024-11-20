from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path("", views.user, name="user"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('register/', views.register, name='register'),
    path('top-up/', views.top_up, name='top_up'), 
]