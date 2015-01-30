from django import template
from django.template import Template

from clockwork.profiles.models import Application

register = template.Library()

@register.simple_tag()
def application_count():
    open_apps = Application.objects.filter(status="open").count()
    return open_apps
