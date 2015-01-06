# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_userprofile__is_applicant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='_is_applicant',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='submitted_app',
        ),
    ]
