from django.views.generic.detail import DetailView

from .forms import ApplicationForm
from .models import UserProfile

def ApplicationFormView(request):
    return render(request, 'app_form.html', {'form': ApplicationForm()})
