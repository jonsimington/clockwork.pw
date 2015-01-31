from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import Group
import markdown
import bleach

from pybb.profiles import PybbProfile

class UserProfile(PybbProfile):
    user = models.OneToOneField(User, related_name="profile")

    about_me = models.TextField(validators=[MaxLengthValidator(500)], null=True, blank=True)
    rendered_about_me = models.TextField(editable=False,
                                         null=True)
    submitted_app = models.NullBooleanField(default=False, blank=True, null=True)
    
    @models.permalink
    def get_absolute_url(self):
        return ('view_profile', (), {'username': self.user.username})

    @property
    def is_applicant(self):
        return self.groups.filter(name="Applicant").exists()

    @property
    def can_view_applications(self):
        groups = ['Member', 'Officer']
        return self.groups.filter(name__in=groups).exists()
    
    @property
    def has_submitted_app(self):
        print "{}'s submitted_app = {}".format(self, self.submitted_app)
        return self.submitted_app
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        try:
            instance.groups.add(Group.objects.get(name='Applicant'))
            Application.objects.create(user=instance)
        except:
            pass


@receiver(pre_save, sender=UserProfile)
def user_profile_pre_save(sender, instance, **kwargs):
    clean_rendered = bleach.clean(instance.about_me,
                                  tags=settings.ALLOWED_HTML_TAGS,
                                  attributes=settings.ALLOWED_HTML_ATTRS)
    instance.rendered_about_me = clean_rendered


# A user's application for more access to the site
class Application(models.Model):
    user = models.OneToOneField(User, related_name="application")

    status = models.CharField(max_length=10, default="open")
    main_character = models.CharField(max_length=12, default="")
    armory_link = models.CharField(max_length=100, default="")
    char_class = models.CharField(max_length=15, default="")
    over_18 = models.CharField(max_length=4, default="")
    char_spec = models.CharField(max_length=15, default="")
    recent_parses = models.TextField(validators=[MaxLengthValidator(500)], default="")
    computer_specs = models.TextField(validators=[MaxLengthValidator(1000)], default="")
    screenshot = models.TextField(max_length=200, default="")
    addons = models.TextField(validators=[MaxLengthValidator(1000)], default="")
    experience = models.TextField(validators=[MaxLengthValidator(1000)], default="")
    how_did_you_hear = models.TextField(validators=[MaxLengthValidator(500)], default="")
    authenticator = models.CharField(max_length=5, default="")
    previous_guild = models.TextField(validators=[MaxLengthValidator(500)], default="")
    battle_tag = models.CharField(max_length=20, default="")
