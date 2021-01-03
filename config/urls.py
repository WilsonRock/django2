from django.contrib import admin
from django.urls import include, path
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,views


from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('users/', include('django.contrib.auth.urls')),  # sistemas de autenticación de django
]  +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# agregamos acciones de usuarios (login,logout)
from django.contrib.auth import views as auth_views

urlpatterns += [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   # path('home2', auth_views.homeView.as_view(), name='home2'),
    
    # path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    
    path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name='users/reset_pass.html'), 
         name='reset_password'),    
]

# agregamos acciones propias
from . import views

urlpatterns += [
    # homapage
    path('', views.home, name='home'),
    path('hm/', views.home, name='hm'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
]
