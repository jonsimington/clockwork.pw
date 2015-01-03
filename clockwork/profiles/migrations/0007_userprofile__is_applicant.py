# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20150103_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='_is_applicant',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
