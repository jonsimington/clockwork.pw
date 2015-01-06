# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20150105_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='age',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='char_race',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='over_18',
            field=models.CharField(default=b'', max_length=4, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='previous_guild',
            field=models.TextField(default=b'', null=True, blank=True, validators=[django.core.validators.MaxLengthValidator(500)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='screenshot',
            field=models.TextField(default=b'', max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]
