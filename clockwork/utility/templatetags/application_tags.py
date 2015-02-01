from django import template
from django.template import Template
from django.contrib.auth.models import Group

from clockwork.profiles.models import Application

register = template.Library()

@register.simple_tag
def open_application_count():
    open_apps = Application.objects.filter(status="open").count()
    if open_apps > 0:
        return '<span class="badge">' + str(open_apps) + "</span>"
    else:
        return ""

@register.simple_tag
def trial_application_count():
    trial_apps = Application.objects.filter(status="trial").count()
    if trial_apps > 0:
        return '<span class="badge">' + str(trial_apps) + "</span>"
    else:
        return ""
    
@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False
