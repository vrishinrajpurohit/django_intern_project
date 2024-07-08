from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path
from .views import Signupview,ProfileView,ProfileUpdateView,ProfileDeleteView
from django.contrib.auth.views import LoginView
from .forms import EmailOrUsernameAuthenticationForm

urlpatterns = [
    path('home',TemplateView.as_view(template_name='home.html'),name='home'),
    path('login/',LoginView.as_view(authentication_form=EmailOrUsernameAuthenticationForm),name='login'),
    path('signup/', Signupview.as_view(),name="signup"),
    path('profile/', ProfileView.as_view(),name="hosthome"),
    path('profile/update', ProfileUpdateView.as_view(),name="profileupdate"),
    path('profile/delete', ProfileDeleteView.as_view(),name="profiledelete"),

]
