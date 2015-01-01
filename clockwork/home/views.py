from django.views.generic import TemplateView
from zinnia.models.entry import Entry

# View for /
class HomePageView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        entries = Entry.published.all()[:5]
        context["entries"] = entries
        return context
