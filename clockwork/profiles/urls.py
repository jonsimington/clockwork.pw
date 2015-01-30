from django.conf.urls import patterns, url
from django.contrib.auth.decorators import permission_required

from .views import (ProfileListView, ProfileView, 
                    MyProfileView, ProfileUpdateView,
                    ApplicationSubmitView, ApplicationFailView,
                    ApplicationsView,)

urlpatterns = patterns(
    '',
    url(r'^roster/$',
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

    url(r'application/submit/$',
        ApplicationSubmitView.as_view(success_url="/application/submit"),
        name='submit_app'),

    url(r'application/update/$',                                                       
        ApplicationSubmitView.as_view(),                                              
        name='update_app'), 

    url(r'application/access-denied/',
        ApplicationFailView.as_view(),
        name='application_fail'),

    url(r'applications/',
        ApplicationsView.as_view(),
        name='applications'),
)
