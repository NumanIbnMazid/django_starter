from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# third party urls
from config.urls_third_party import urlpatterns as THIRD_PARTY_URL_PATTERNS

# Views
from config.views import HomeView

APP_URL_PATTERNS = [
    # App URL Patterns
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
] + THIRD_PARTY_URL_PATTERNS + APP_URL_PATTERNS

if settings.DEBUG:
    # Static and Media URL
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)