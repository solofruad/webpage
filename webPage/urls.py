from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webPage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$','principal.views.inicio'), 
	url(r'^sobre/$','principal.views.sobre'), 
	url(r'^servicios/$','principal.views.servicios'), 
	url(r'^contacto/$','principal.views.contacto'), 
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
