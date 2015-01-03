# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_userprofile_addons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.CharField(default=b'', max_length=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='authenticator',
            field=models.CharField(default=b'', max_length=5),
            preserve_default=True,
        ),
    ]
