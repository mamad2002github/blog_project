from . import views
from django.urls import path


app_name = 'Account'
urlpatterns=[
    path('login/',views.sign_in,name = 'loginnn'),
    path('logout',views.user_logout,name = 'logout'),
    path ('register', views.user_register,name='register'),

]