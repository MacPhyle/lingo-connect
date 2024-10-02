"""
URL configuration for vehiclecollector project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .forms import CustomAuthenticationForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('calendar/', views.current_month_calendar_view, name='calendar'),
    path('calendar/<int:year>/<int:month>/', views.calendar_view, name='calendar_view'),
    path('calendar/<int:year>/<int:month>/<int:day>/', views.date_details, name='date_details'),
    path('calendar/create_event/', views.create_event, name='create_event'),
    path('update/<int:id>/', views.update_event, name='update_event'),
    path('delete/<int:id>/', views.delete_event, name='delete_event'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('chat/', views.chat, name='chat'),
    path('forum/', views.forum, name='forum'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('contact/', views.contact, name='contact'),
    path('learning_apps/', views.learning_apps, name='learning_apps'),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
