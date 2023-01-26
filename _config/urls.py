"""_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import views
from django.urls import path, include

from home.sitemap import home_sitemap

sitemaps = dict([home_sitemap])

urlpatterns = [
    # Django.
    path('admin/', admin.site.urls),
    path(route='accounts/', view=include('django.contrib.auth.urls')),
    # Sitemap.
    path(
        route='sitemap.xml',
        view=views.index,
        kwargs={'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.index',
    ),
    path(
        route='sitemap-<section>.xml',
        view=views.sitemap,
        kwargs={'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap',
    ),
    # Apps.
    path(route='', view=include('home.urls')),
    path(route='accounts/', view=include('accounts.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(
        path(route='__debug__/', view=include(debug_toolbar.urls)),
    )
    urlpatterns += static(prefix=settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(prefix=settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
