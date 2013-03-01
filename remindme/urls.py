from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'reminders.views.home'),
    url(r'^mobile/', 'reminders.views.mobile'),
    url(r'^admin/', include(admin.site.urls)),
)
