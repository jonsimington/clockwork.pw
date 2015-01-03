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

    about_me = models.TextField(validators=[MaxLengthValidator(500)])
    rendered_about_me = models.TextField(editable=False,
                                         null=True)

    main_character = models.CharField(max_length=12, default="")
    armory_link = models.CharField(max_length=100, default="")
    char_race = models.CharField(max_length=15, default="")
    char_class = models.CharField(max_length=15, default="")
    age = models.CharField(max_length=3, default="")
    char_spec = models.CharField(max_length=15, default="")
    recent_parses = models.TextField(validators=[MaxLengthValidator(500)], default="")
    computer_specs = models.TextField(validators=[MaxLengthValidator(1000)], default="")
    screenshot = models.CharField(max_length=100, default="")
    addons = models.TextField(validators=[MaxLengthValidator(1000)], default="")
    experience = models.TextField(validators=[MaxLengthValidator(1000)], default="")
    how_did_you_hear = models.CharField(max_length=100, default="")
    authenticator = models.CharField(max_length=5, default="")

    submitted_app = models.BooleanField(default=False)
    
    @models.permalink
    def get_absolute_url(self):
        return ('view_profile', (), {'username': self.user.username})


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
