# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20150105_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='submitted_app',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
