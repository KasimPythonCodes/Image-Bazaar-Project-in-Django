"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
#
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
from django.conf import settings
from django.conf.urls.static import static

from enroll import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.Home_Page , name='home'),
    path('', views.Sign_Page , name='sign'),
    path('login/', views.Login_Page , name='login'),
    path('logout/', views.Logout_Page , name='logout'),
    path('changepass/', views.ChangePaas, name='changepass'),
    path('setpass/', views.Set_pass_Form, name='setpass'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
