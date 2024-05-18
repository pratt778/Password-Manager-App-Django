from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name="home"),
    path('login',views.loginUser,name="login"),
    path('signup',views.signup,name="signup"),
    path('logout',views.loguser,name="logout"),
    path('mylist',views.mylist,name='mylist'),
    path('prac',views.prac,name="practice"),
]
