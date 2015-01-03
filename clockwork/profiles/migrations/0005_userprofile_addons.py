# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_userprofile_submitted_app'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='addons',
            field=models.TextField(default=b'', validators=[django.core.validators.MaxLengthValidator(1000)]),
            preserve_default=True,
        ),
    ]
