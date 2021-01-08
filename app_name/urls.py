from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [

    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('signup/',views.signup,name="signup"),
    path('apply/',views.apply,name="apply")

]