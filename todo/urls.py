from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login_user, name="login"),
    path('register', views.register_user, name="register"),
    path('logout', views.logout_user, name="logout"),

    path('new/', views.new_todo, name="new"),
    path('done/<int:pk>/', views.done_todo, name="done"),
    path('delete/<int:pk>/', views.delete_todo, name="delete"),
]
