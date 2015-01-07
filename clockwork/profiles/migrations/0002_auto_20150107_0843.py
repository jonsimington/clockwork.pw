# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='addons',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='armory_link',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='authenticator',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='char_class',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='char_spec',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='computer_specs',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='how_did_you_hear',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='main_character',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='over_18',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='previous_guild',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='recent_parses',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='screenshot',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='submitted_app',
        ),
    ]
