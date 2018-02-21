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
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter

from checkout.views import CheckoutView
from contact.views import ContactView
from profiles.views import ProfileView
from tryTen.views import AboutView

ROUTER = DefaultRouter()

urlpatterns = [
    url(r'^api/', include(ROUTER.urls)),
    url(r'^$', RedirectView.as_view(pattern_name='goods:goods:list'), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^goods/', include('goods.urls', namespace='goods')),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^profile/$', ProfileView.as_view(), name='profile'),
    url(r'^checkout/$', CheckoutView.as_view(), name='checkout'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^taggit/', include('taggit_selectize.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# TODO: Implement 2FA & update corresponding Cover letter
# TODO: Implement TBA using django-allauth & update corresponding Cover letter
