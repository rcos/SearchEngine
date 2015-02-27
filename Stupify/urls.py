from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Stupify.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'Stupify.views.home', name='home'),
    url(r'^manage/', 'Stupify.views.manage', name='manage'),
    url(r'^vote/(\d+)$', 'Stupify.views.vote', name='vote'),
    url(r'^delete/(\d+)$', 'Stupify.views.delete', name='delete'),
)
