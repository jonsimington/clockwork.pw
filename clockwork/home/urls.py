from django.conf.urls import patterns, url

from views import HomePageView, AboutUsView, BlogView, MediaView

urlpatterns = patterns(
    '',
    url(r'^$', HomePageView.as_view(), name="home"),

    url(r'^about-us/$', AboutUsView.as_view(), name="about_us"),

    url(r'^blog/$', BlogView.as_view(), name="blog"),

    url(r'^media/$', MediaView.as_view(), name="media"),
)
