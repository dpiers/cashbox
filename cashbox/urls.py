from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^cashbox/', include('cashbox.foo.urls')),
    url(r'^$', 'cashbox.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),
)
