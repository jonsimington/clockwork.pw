from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # home app
    url(r'^', include('clockwork.home.urls'),

    # user profiles
    url(r'^', include('clockwork.profiles.urls'),
)
