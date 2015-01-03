# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20141231_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='armory_link',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='authenticator',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='char_class',
            field=models.CharField(default=b'', max_length=15),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='char_race',
            field=models.CharField(default=b'', max_length=15),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='char_spec',
            field=models.CharField(default=b'', max_length=15),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='computer_specs',
            field=models.TextField(default=b'', validators=[django.core.validators.MaxLengthValidator(1000)]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='experience',
            field=models.TextField(default=b'', validators=[django.core.validators.MaxLengthValidator(1000)]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='how_did_you_hear',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='main_character',
            field=models.CharField(default=b'', max_length=12),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='recent_parses',
            field=models.TextField(default=b'', validators=[django.core.validators.MaxLengthValidator(500)]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='screenshot',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
