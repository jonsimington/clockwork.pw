from django import template
from django.template import Template
from django.utils import timezone

import datetime

from clockwork.profiles.models import Application

register = template.Library()

@register.simple_tag
def open_application_count():
    open_apps = Application.objects.filter(status="open").filter(user__profile__submitted_app="True")
    open_count = open_apps.count()

    if open_apps > 0:
        return '<span class="badge">' + str(open_count) + "</span>"
    else:
        return ""

@register.simple_tag
def trial_application_count():
    trial_apps = Application.objects.filter(status="trial").filter(user__profile__submitted_app="True")
    trial_count = trial_apps.count()
    
    if trial_apps > 0:
        return '<span class="badge">' + str(trial_count) + "</span>"
    else:
        return ""

@register.simple_tag
def updated_submitted_timestamp(application):
    submitted = application.submitted
    updated = application.updated
    default = datetime.datetime(2000, 1, 1, 6, 0, tzinfo=timezone.utc)

    submitted_strf = submitted.strftime("%B %d %Y, %I:%M %p")
    updated_strf = updated.strftime("%B %d %Y, %I:%M %p")
    
    if submitted != default:
        # Check if only submitted once (updated == submitted)
        if updated == default:
            return '<span class="label label-default">Submitted {}</span>'.format(submitted_strf) 
        else:
            return '<span class="label label-primary">Updated {}</span>&nbsp;<span class="label label-default">Submitted {}</span>'.format(updated_strf, submitted_strf) 
    else:
        return ""
