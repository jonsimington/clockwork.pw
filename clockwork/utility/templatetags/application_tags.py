from django import template
from django.template import Template

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
