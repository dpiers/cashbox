from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('cashbox.core.views',

    url(r'^$', 'landing'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),

)
