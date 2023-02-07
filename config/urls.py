from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# Adds site header, site title, index title to the admin side.
admin.site.site_header = 'Central WebFilter'
admin.site.site_title = 'Saltis WebFilter'
admin.site.index_title = 'Saltis WebFilter'

urlpatterns = [
    path('/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('webfilters/', include('webfilters.urls')),
]

'''
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns() # tell gunicorn where static files are in dev mode
    urlpatterns += static(settings.MEDIA_URL + 'media/', document_root=os.path.join(settings.MEDIA_ROOT, 'media'))
    urlpatterns += [
        path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'myapp/images/favicon.ico'))
    ]
'''
