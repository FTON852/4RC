from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('main.urls', 'main'), namespace='main')),
    path('market/', include('marketplace.urls'), name='market'),
    path('accounts/', include('allauth.urls')),
    path('feed/', include('eventfeed.urls')),
    path('tasks/', include(('gamification.urls', 'gamification'), namespace='gamification')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
