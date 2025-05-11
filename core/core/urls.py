"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from event_management_system_app import views
from event_management_system_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.category_list, name='category_list'),
    #path('filter/<str:name>', views.filter_list, name='filter_list'),
    path('categories/create/', views.create_category, name='create_category'),
    path('categories/<int:category_id>/', views.category_events, name='category_events'),
    path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),
    path('events/create/', views.create_event, name='create_event'),
    path('events/update/<int:event_id>/', views.update_event, name='update_event'),
    path('events/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('event-chart/', views.event_chart, name='event_chart'),
    path("login/",login_page,name="login-page"),
    path("register/",register_page,name="register-page"),
    path("login/",log_out,name="login-page"),
]