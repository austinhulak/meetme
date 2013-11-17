from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'meetme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('social_auth.urls')),

    url(r'^$', 'meetme.views.main', name='main'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^privacy/$', 'meetme.views.privacy', name='privacy'),
    url(r'^terms/$', 'meetme.views.terms', name='terms'),
    url(r'^support/$', 'meetme.views.support', name='support'),

    url(r'^logout/', 'meetme.views.logout', name='logout'),
)
