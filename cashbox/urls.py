from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('cashbox.core.views',

    url(r'^$', 'landing'),
    url(r'^hack/$', 'index'),

    url(r'^beta_mailinglist/signup/$', 'ajax_beta_mailing_list_signup'),
    url(r'^email_ryan/$', 'ajax_email_ryan'),

)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^singly/', include('singly.urls')),

)
