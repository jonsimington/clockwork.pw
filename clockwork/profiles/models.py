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

    main_character = models.CharField(max_length=12, default="", blank=True, null=True)
    armory_link = models.CharField(max_length=100, default="", blank=True, null=True)
    char_class = models.CharField(max_length=15, default="", blank=True, null=True)
    over_18 = models.CharField(max_length=4, default="", blank=True, null=True)
    char_spec = models.CharField(max_length=15, default="", blank=True, null=True)
    recent_parses = models.TextField(validators=[MaxLengthValidator(500)], default="", blank=True, null=True)
    computer_specs = models.TextField(validators=[MaxLengthValidator(1000)], default="", blank=True, null=True)
    screenshot = models.TextField(max_length=200, default="", blank=True, null=True)
    addons = models.TextField(validators=[MaxLengthValidator(1000)], default="", blank=True, null=True)
    experience = models.TextField(validators=[MaxLengthValidator(1000)], default="", blank=True, null=True)
    how_did_you_hear = models.TextField(validators=[MaxLengthValidator(500)], default="", blank=True, null=True)
    authenticator = models.CharField(max_length=5, default="", blank=True, null=True)
    submitted_app = models.NullBooleanField(default=False, blank=True, null=True)
    previous_guild = models.TextField(validators=[MaxLengthValidator(500)], default="", blank=True, null=True)
    
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
        instance.groups.add(Group.objects.get(name='Applicant'))


@receiver(pre_save, sender=UserProfile)
def user_profile_pre_save(sender, instance, **kwargs):
    # Render the about_me field as HTML instead of markdown
    rendered = markdown.markdown(instance.about_me, safe_mode='escape')
    clean_rendered = bleach.clean(rendered,
                                  tags=settings.ALLOWED_HTML_TAGS,
                                  attributes=settings.ALLOWED_HTML_ATTRS)
    instance.rendered_about_me = clean_rendered
