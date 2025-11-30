from django.urls import path
from .views import *
from django.contrib.auth.views import *
from idea import views

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('accounts/login/', login_page, name='login'),
    path('signup/', signup_page, name='signup'),
    path('firstpage/', views.Firstpage.as_view(), name='firstpage'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('search/', views.search, name='search'),
    path('explore/', views.explore, name='explore'),
    path('profile/', views.profile, name='profile'),
]