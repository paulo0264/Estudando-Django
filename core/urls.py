from django.conf.urls import *
from django.urls import path
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.conf import settings

from django.contrib import admin
from proposta import views


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


