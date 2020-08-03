from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(extra_context={'next': '/account/profile'})),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]
