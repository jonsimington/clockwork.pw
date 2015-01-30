from django import template
from django.template import Template

from clockwork.profiles.models import Application

register = template.Library()

@register.simple_tag()
def application_count():
    open_apps = Application.objects.filter(status="open").count()
    if open_apps > 0:
        return '<span class="badge">' + str(open_apps) + "</span>"
    else:
        return ""
