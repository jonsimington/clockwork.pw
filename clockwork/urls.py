from django.conf import settings
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

    # blog
    url(r'^blog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),

    #forums
    url(r'^forums/', include('pybb.urls', namespace='pybb')),

    # pybb avatars
    url(r'^pybb/(?P<path>.*\.png)$', 'django.views.static.serve',
            {'document_root': settings.AVATAR_DIR}),
)
