from django.views.generic import TemplateView
from zinnia.models.entry import Entry

# View for /
class HomePageView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context["entries"] = Entry.published.all()[:5]
        return context

class AboutUsView(TemplateView):
    template_name = "home/about-us.html"

class BlogView(TemplateView):
    template_name = "home/blog.html"

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['entries'] = Entry.published.all()
        return context

class MediaView(TemplateView):
    template_name = "home/media.html"
