from django.conf.urls import patterns, url
from django.contrib.auth.decorators import permission_required

from .views import (RosterView, ProfileView, 
                    MyProfileView, ProfileUpdateView,
                    ApplicationSubmitView, ApplicationSubmittedView,
                    ApplicationFailView, ApplicationsView,
                    ApplicationUpdateView, DeclinedApplicationView,)

urlpatterns = patterns(
    '',
    url(r'^roster/$',
        RosterView.as_view(),
        name="roster"),

    url(r'^profile/$',
        MyProfileView.as_view(),
        name="view_profile"),
    
    url(r'^profiles/(?P<username>.+)/$',
        ProfileView.as_view(),
        name="view_profile"),

    url(r'^profile/edit/$',
        ProfileUpdateView.as_view(),
        name="update_profile"),

    url(r'^application/submit/$',
        ApplicationSubmitView.as_view(success_url="/application/submitted"),
        name='submit_app'),

    url(r'^application/submitted/$',
        ApplicationSubmittedView.as_view(),
        name='submitted_app'),

    url(r'^application/update/$',                                                       
        ApplicationSubmitView.as_view(),                                              
        name='update_app'), 

    url(r'^application/access-denied/',
        ApplicationFailView.as_view(),
        name='application_fail'),

    url(r'^applications/(?P<type>[\w-]+)/',
        ApplicationsView.as_view(),
        name='applications'),
    
    url(r'^application/(?P<applicant_name>[\w-]+)/(?P<rank>[\w-]+)/',
        ApplicationUpdateView.as_view(),
        name='update_app'),

    url(r'^application/declined/',
        DeclinedApplicationView.as_view(),
        name='declined_app'),
)
