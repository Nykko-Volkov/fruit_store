from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login_user'),
    path("logout/", views.logout_view, name="logout"),

   
] 
