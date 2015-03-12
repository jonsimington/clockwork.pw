from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.base import TemplateView, View
from django.http import Http404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth import models
from django.contrib.auth.models import User, Group

from .models import UserProfile, Application
from .forms import UserProfileForm, ApplicationForm

class RosterView(ListView):
    template_name = "profiles/roster.html"
    model = UserProfile
    context_object_name = "userprofiles"
    
    def dispatch(self, request, *args, **kwargs):
        # only authenticated users can access this view
        return super(RosterView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RosterView, self).get_context_data(**kwargs)
        allowed_groups = ['Trial', 'Member', 'Officer']
        
        context['deathknights'] = Application.objects.filter(char_class="Death Knight").filter(user__groups__name__in=allowed_groups)
        context['druids'] = Application.objects.filter(char_class="Druid").filter(user__groups__name__in=allowed_groups)
        context['hunters'] = Application.objects.filter(char_class="Hunter").filter(user__groups__name__in=allowed_groups)
        context['mages'] = Application.objects.filter(char_class="Mage").filter(user__groups__name__in=allowed_groups)
        context['monks'] = Application.objects.filter(char_class="Monk").filter(user__groups__name__in=allowed_groups)
        context['paladins'] = Application.objects.filter(char_class="Paladin").filter(user__groups__name__in=allowed_groups)
        context['priests'] = Application.objects.filter(char_class="Priest").filter(user__groups__name__in=allowed_groups)
        context['rogues'] = Application.objects.filter(char_class="Rogue").filter(user__groups__name__in=allowed_groups)
        context['shamans'] = Application.objects.filter(char_class="Shaman").filter(user__groups__name__in=allowed_groups)
        context['warlocks'] = Application.objects.filter(char_class="Warlock").filter(user__groups__name__in=allowed_groups)
        context['warriors'] = Application.objects.filter(char_class="Warrior").filter(user__groups__name__in=allowed_groups)

        return context
    
    def get_queryset(self):
        return UserProfile.objects.exclude(user__id=-1).order_by('user__groups__id')
    
class ProfileView(DetailView):
    """ A view that displays a user's profile.
    """
    template_name = "profiles/view_profile.html"
    context_object_name = "userprofile"
    model = UserProfile

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        """Ensures that only authenticated users can access the view."""
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        try:
            username = self.kwargs['username']
            return queryset.get(user__username=username)
        except UserProfile.DoesNotExist:
            raise Http404("User profile doesn't exist for user %s" % username)


class MyProfileView(ProfileView):
    """ A view that displays a user's own profile.
    """
    def get_object(self, queryset=None):
        try:
            return self.request.user.profile
        except UserProfile.DoesNotExist:
            user = self.request.user
            logger.info("Creating user profile for %s" % user.username)
            return UserProfile.objects.create(user=user)

class ProfileUpdateView(UpdateView):
    """ A view that displays a form for editing a user's profile.
    """
    template_name = "profiles/update_profile.html"
    form_class = UserProfileForm
    context_object_name = "userprofile"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        """Ensures that only authenticated users can access the view."""
        return super(ProfileUpdateView, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        return self.request.user.profile

    def get_initial(self):
        initial = super(ProfileUpdateView, self).get_initial()
        initial['first_name'] = self.request.user.first_name
        initial['last_name'] = self.request.user.last_name
        initial['email'] = self.request.user.email
        return initial

    def form_valid(self, form):
        messages.success(self.request, "Profile updated")
        return super(ProfileUpdateView, self).form_valid(form)

def applicant_check(user):
    return user.groups.filter(name='Applicant').exists()

# Returns True if user is allowed to edit their application info
def can_edit_application(user):
    groups = ["Declined", "Applicant", "Member", "Officer"]
    return user.groups.filter(name__in=groups).exists()

def staff_check(user):
    return user.is_staff

def member_check(user):
    groups = ['Officer', 'Member']
    return user.groups.filter(name__in=groups).exists()

class ApplicationSubmitView(UpdateView):
    """
        A view that displays the application form to be submitted or updated
    """
    
    template_name = "profiles/application_form.html"
    form_class = ApplicationForm
    context_object_name = "application"

    @method_decorator(user_passes_test(can_edit_application, login_url="application/access-denied/"))
    def dispatch(self, request, *args, **kwargs):
        return super(ApplicationSubmitView, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        return self.request.user.application

    def form_valid(self, form):
        return super(ApplicationSubmitView, self).form_valid(form)

    def get_form_kwargs( self ):
        kwargs = super( ApplicationSubmitView, self ).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class ApplicationSubmittedView(TemplateView):
    template_name = "profiles/application_submitted.html"
    
class ApplicationsView(TemplateView):
    """
    A view that displays all open applications to admins
    """

    template_name = "profiles/applications.html"
    
    @method_decorator(user_passes_test(member_check, login_url="application/access-denied/"))
    def dispatch(self, *args, **kwargs):
        return super(ApplicationsView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ApplicationsView, self).get_context_data(**kwargs)
        app_type = kwargs.pop('type')

        if app_type == 'open':
            group = models.Group.objects.get(name='Applicant')
            users = group.user_set.filter(application__status=app_type)
        elif app_type == 'trial':
            group = models.Group.objects.get(name='Trial')
            users = group.user_set.filter(application__status=app_type)
        context['applicants'] = users.filter(profile__submitted_app="True")
        context['app_type'] = app_type
        return context
    
class ApplicationFailView(TemplateView):
    template_name = "profiles/app_denied.html"

class ApplicationUpdateView(UpdateView):
    @method_decorator(user_passes_test(staff_check, login_url="application/access-denied/"))
    def dispatch(self, *args, **kwargs):
        return super(ApplicationUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, **kwargs):
        applicant_name = kwargs.pop('applicant_name')
        rank = kwargs.pop('rank')
        rank_title = rank.title()
        applicant = User.objects.get(username=applicant_name)

        if rank == 'accepted':
            group = Group.objects.get(name="Member")
        else:
            group = Group.objects.get(name=rank_title)
        
        # Update user's application status
        applicant.application.status = rank
        applicant.application.save()

        # Change user's group 
        current_group = applicant.groups.first()
        applicant.groups.remove(current_group)
        if group == "Accepted":
            group = "Member"
        applicant.groups.add(group)
        applicant.save()

class DeclinedApplicationView(TemplateView):
    template_name="profiles/declined_application.html"
