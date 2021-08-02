from django.conf.urls import handler404, handler403, handler500
from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from .views import *
# from django.conf.urls.static import static
#from django.conf.urls.i18n import i18n_patterns

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.contrib.sitemaps.views import sitemap

urlpatterns = [
    path('', home, name="home"),
    path('cpanel/', admin.site.urls),

    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),


    path('full-page/', full, name="full"),
    path('about/', about, name="about"),
    path('menu/', menu, name="menu"),
    path('specials/', specials, name="specials"),
    path('events/', events, name="events"),
    path('chefs/', chefs, name="chefs"),
    path('gallery/', gallery, name="gallery"),
    path('contact/', contact, name="contact"),
    path('book-a-table/', book, name="book"),
    
    path('sitemap.xml', sitemap),

]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
