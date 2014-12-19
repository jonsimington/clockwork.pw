from django.conf.urls import patterns, url

from .views import (ProfileListView, ProfileView, 
                    MyProfileView, ProfileUpdateView)

urlpatterns = patterns(
    '',
    url(r'^profiles/$',
        ProfileListView.as_view(),
        name="list_profile"),

    url(r'^profile/$',
        MyProfileView.as_view(),
        name="view_profile"),
    
    url(r'^profiles/(?P<username>.+)/$',
        ProfileView.as_view(),
        name="view_profile"),

    url(r'^profile/edit/$',
        ProfileUpdateView.as_view(),
        name="update_profile"),
)
