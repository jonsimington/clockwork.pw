from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import logout_then_login

admin.autodiscover()

urlpatterns = patterns(
    '',
    
    # /admin
    url(r'^admin/', include(admin.site.urls)),

    # home app urls
    url(r'^', include('clockwork.home.urls')),

    # user profiles urls
    url(r'^', include('clockwork.profiles.urls')),

    # Django AllAuth
    url(r'^accounts/logout/$', logout_then_login),
    url(r'^accounts/', include('allauth.urls')),

)
