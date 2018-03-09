"""tryTen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from rest_framework.routers import DefaultRouter

from checkout.views import CheckoutView
from contact.views import ContactView
from profiles.views import ProfileView

ROUTER = DefaultRouter()

urlpatterns = [
    path('api/', include(ROUTER.urls)),
    path('', RedirectView.as_view(pattern_name='goods:list'), name='home'),
    path('admin/', admin.site.urls),
    path('goods/', include('goods.urls', namespace='goods')),
    path('categories/', include('categories.urls', namespace='categories')),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('accounts/', include('allauth.urls')),
    path('taggit/', include('taggit_selectize.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# TODO: Implement 2FA & update corresponding Cover letter
# TODO: Implement TBA using django-allauth & update corresponding Cover letter
