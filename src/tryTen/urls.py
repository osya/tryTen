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
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from profiles import views as profiles_views
from contact import views as contact_vies
from checkout import views as checkout_views
from goods import views as goods_views
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^goods/', include('goods.urls', namespace='goods')),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^profile/$', profiles_views.ProfileView.as_view(), name='profile'),
    url(r'^checkout/$', checkout_views.CheckoutView.as_view(), name='checkout'),
    url(r'^contact/$', contact_vies.ContactView.as_view(), name='contact'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^(?:category/(?P<pk>\d+)/)?(?:page/(?P<page>\d+))?$', goods_views.GoodList.as_view(), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# TODO: Implement 2FA & update corresponding Cover letter
# TODO: Implement TBA using django-allauth & update corresponding Cover letter
