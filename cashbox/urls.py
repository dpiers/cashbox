from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('cashbox.core.views',

    url(r'^$', 'landing'),
    url(r'^hack/$', 'index'),

)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^singly/', include('singly.urls')),

)
