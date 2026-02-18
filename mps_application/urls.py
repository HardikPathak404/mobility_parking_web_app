from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('condition/', views.condition, name='condition'),
    path('profile/', views.profile, name='profile'),
    path('sectionOne/', views.sectionOne, name='sectionOne'),
    path('sectionTwo/<int:application_id>/', views.sectionTwo, name='sectionTwo'),
    path('sectionThree/<int:application_id>/', views.sectionThree, name='sectionThree'),
    path('applications/', views.show_applicantion, name='applications'),
    path('registration/', views.create_user, name='register'), 
    path('logout/submit/', views.logout_view, name='logout'),
    path('logout/', views.logout_confirmation, name='logout_confirmation'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]