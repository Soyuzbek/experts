from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from items.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('items/', include(('items.urls', 'items'), 'items')),
    path('translate/', include('rosetta.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)