from django.views.generic import TemplateView

# View for /
class HomePageView(TemplateView):
    template_name = "home/home.html"
