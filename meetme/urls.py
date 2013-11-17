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
    url(r'^category/(?P<category_id>\d+)/$', 'meetme.views.category', name='category'),
    url(r'^profile/(?P<profile_id>\d+)/$', 'meetme.views.profile', name='profile'),
 
    url(r'^have_fun/$', 'meetme.views.have_fun', name='have_fun'),

    # ajax requests to handle buttons
    url(r'^im_available/$', 'meetme.views.im_available', name='im_available'),
    url(r'^make_request/$', 'meetme.views.make_request', name='make_request'),

    url(r'^privacy/$', 'meetme.views.privacy', name='privacy'),
    url(r'^terms/$', 'meetme.views.terms', name='terms'),
    url(r'^set_phone/$', 'meetme.views.set_phone', name='set_phone'),
    url(r'^show_reservation/(?P<reservation_id>\d+)/$', 'meetme.views.show_reservation', name='show_reservation'),
    url(r'^support/$', 'meetme.views.support', name='support'),

    url(r'^login/$', 'meetme.views.login', name='login'),
    url(r'^logout/', 'meetme.views.logout', name='logout'),
)
