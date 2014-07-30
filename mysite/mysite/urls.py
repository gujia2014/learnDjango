from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from mysite.views import hello, current_datetime, hours_ahead
import datetime

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('^hello/$', hello),
    url('^time/$', current_datetime),
    url('^another-time-page/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead)
)

urlpatterns += patterns('addApi.views',
    url(r'^myapi/add_publisher$', 'add_publisher', name='add_publisher'),
    url(r'^myapi/update_publisher$', 'update_publisher', name='update_publisher'),
)
