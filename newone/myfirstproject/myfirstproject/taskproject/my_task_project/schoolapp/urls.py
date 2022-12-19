from django.urls import path
from . import views

app_name='schoolapp'

urlpatterns = [
    path('',views.home,name='home'),
    path('login/', views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('Forms/',views.Forms,name='Forms')
]
