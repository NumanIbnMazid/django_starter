from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views import defaults as default_views

# third party urls
from config.urls_third_party import urlpatterns as THIRD_PARTY_URL_PATTERNS

# Views
from config.views import HomeView

APP_URL_PATTERNS = [
    # App URL Patterns
    path('', HomeView.as_view(), name='home'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
] + THIRD_PARTY_URL_PATTERNS + APP_URL_PATTERNS

if settings.DEBUG:
    # Static and Media URL
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # This allows the error pages to be debugged during development
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
