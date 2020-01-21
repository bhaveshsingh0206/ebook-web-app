"""Ebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from Users import views as user_view
from django.contrib.auth import views as auth_view
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Books/', include('Books.urls')),
    url(r'^register/', user_view.register, name='register'),

    url(r'^login', auth_view.LoginView.as_view(template_name='Users/logn.html'), name='login'),
    url(r'^logout/', auth_view.LogoutView.as_view(template_name ='Users/logout.html'), name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)