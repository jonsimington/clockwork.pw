from django import template
from django.template import Template
from django.utils import timezone

import datetime
import pytz

from clockwork.profiles.models import Application

register = template.Library()

@register.simple_tag
def open_application_count():
    open_apps = Application.objects.filter(status="open").filter(user__profile__submitted_app="True")
    open_count = open_apps.count()

    if open_count > 0:
        return '<span class="badge">' + str(open_count) + "</span>"
    else:
        return ""

@register.simple_tag
def trial_application_count():
    trial_apps = Application.objects.filter(status="trial").filter(user__profile__submitted_app="True")
    trial_count = trial_apps.count()
    
    if trial_count > 0:
        return '<span class="badge">' + str(trial_count) + "</span>"
    else:
        return ""

@register.simple_tag
def updated_submitted_timestamp(application):
    submitted = application.submitted
    updated = application.updated
    default = datetime.datetime(2000, 1, 1, 0, 0, tzinfo=pytz.utc)

    default_unicode = unicode(default)
    submitted_unicode = unicode(submitted)
    updated_unicode = unicode(updated)

    submitted_strf = submitted.strftime("%B %d %Y, %I:%M %p")
    updated_strf = updated.strftime("%B %d %Y, %I:%M %p")

    # If app is submitted
    if submitted_unicode != default_unicode:
        # Check if only submitted once (updated == submitted)
        if updated_unicode == submitted_unicode:
            return '<span class="label label-default">Submitted {}</span>'.format(submitted_strf) 
        else:
            return '<span class="label label-primary">Updated {}</span>&nbsp;<span class="label label-default">Submitted {}</span>'.format(updated_strf, submitted_strf) 
    else:
        return ""
