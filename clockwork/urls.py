from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    
    # /admin
    url(r'^admin/', include(admin.site.urls)),

    # home app urls
    url(r'^', include('clockwork.home.urls')),

    # user profiles urls
    #url(r'^', include('clockwork.profiles.urls')),
)
