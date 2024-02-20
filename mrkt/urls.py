# Description: This file is used to define the URL patterns for the application.
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from core.views import index, contact

urlpatterns = [
    path('', index, name='index'),
    path('items/', include('item.urls')),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)