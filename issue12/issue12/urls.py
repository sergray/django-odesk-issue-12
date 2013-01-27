from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'issue12.app.views.index'),
    url(r'^odesk_auth/', include('django_odesk.auth.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    # Examples:
    # url(r'^$', 'issue12.views.home', name='home'),
    # url(r'^issue12/', include('issue12.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
