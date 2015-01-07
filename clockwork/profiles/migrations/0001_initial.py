# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import pybb.util
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('signature', models.TextField(max_length=1024, verbose_name='Signature', blank=True)),
                ('signature_html', models.TextField(max_length=1054, verbose_name='Signature HTML Version', blank=True)),
                ('time_zone', models.FloatField(default=3.0, verbose_name='Time zone', choices=[(-12.0, b'-12'), (-11.0, b'-11'), (-10.0, b'-10'), (-9.5, b'-09.5'), (-9.0, b'-09'), (-8.5, b'-08.5'), (-8.0, b'-08 PST'), (-7.0, b'-07 MST'), (-6.0, b'-06 CST'), (-5.0, b'-05 EST'), (-4.0, b'-04 AST'), (-3.5, b'-03.5'), (-3.0, b'-03 ADT'), (-2.0, b'-02'), (-1.0, b'-01'), (0.0, b'00 GMT'), (1.0, b'+01 CET'), (2.0, b'+02'), (3.0, b'+03'), (3.5, b'+03.5'), (4.0, b'+04'), (4.5, b'+04.5'), (5.0, b'+05'), (5.5, b'+05.5'), (6.0, b'+06'), (6.5, b'+06.5'), (7.0, b'+07'), (8.0, b'+08'), (9.0, b'+09'), (9.5, b'+09.5'), (10.0, b'+10'), (10.5, b'+10.5'), (11.0, b'+11'), (11.5, b'+11.5'), (12.0, b'+12'), (13.0, b'+13'), (14.0, b'+14')])),
                ('language', models.CharField(default=b'en-us', max_length=10, verbose_name='Language', blank=True, choices=[(b'af', b'Afrikaans'), (b'ar', b'Arabic'), (b'ast', b'Asturian'), (b'az', b'Azerbaijani'), (b'bg', b'Bulgarian'), (b'be', b'Belarusian'), (b'bn', b'Bengali'), (b'br', b'Breton'), (b'bs', b'Bosnian'), (b'ca', b'Catalan'), (b'cs', b'Czech'), (b'cy', b'Welsh'), (b'da', b'Danish'), (b'de', b'German'), (b'el', b'Greek'), (b'en', b'English'), (b'en-au', b'Australian English'), (b'en-gb', b'British English'), (b'eo', b'Esperanto'), (b'es', b'Spanish'), (b'es-ar', b'Argentinian Spanish'), (b'es-mx', b'Mexican Spanish'), (b'es-ni', b'Nicaraguan Spanish'), (b'es-ve', b'Venezuelan Spanish'), (b'et', b'Estonian'), (b'eu', b'Basque'), (b'fa', b'Persian'), (b'fi', b'Finnish'), (b'fr', b'French'), (b'fy', b'Frisian'), (b'ga', b'Irish'), (b'gl', b'Galician'), (b'he', b'Hebrew'), (b'hi', b'Hindi'), (b'hr', b'Croatian'), (b'hu', b'Hungarian'), (b'ia', b'Interlingua'), (b'id', b'Indonesian'), (b'io', b'Ido'), (b'is', b'Icelandic'), (b'it', b'Italian'), (b'ja', b'Japanese'), (b'ka', b'Georgian'), (b'kk', b'Kazakh'), (b'km', b'Khmer'), (b'kn', b'Kannada'), (b'ko', b'Korean'), (b'lb', b'Luxembourgish'), (b'lt', b'Lithuanian'), (b'lv', b'Latvian'), (b'mk', b'Macedonian'), (b'ml', b'Malayalam'), (b'mn', b'Mongolian'), (b'mr', b'Marathi'), (b'my', b'Burmese'), (b'nb', b'Norwegian Bokmal'), (b'ne', b'Nepali'), (b'nl', b'Dutch'), (b'nn', b'Norwegian Nynorsk'), (b'os', b'Ossetic'), (b'pa', b'Punjabi'), (b'pl', b'Polish'), (b'pt', b'Portuguese'), (b'pt-br', b'Brazilian Portuguese'), (b'ro', b'Romanian'), (b'ru', b'Russian'), (b'sk', b'Slovak'), (b'sl', b'Slovenian'), (b'sq', b'Albanian'), (b'sr', b'Serbian'), (b'sr-latn', b'Serbian Latin'), (b'sv', b'Swedish'), (b'sw', b'Swahili'), (b'ta', b'Tamil'), (b'te', b'Telugu'), (b'th', b'Thai'), (b'tr', b'Turkish'), (b'tt', b'Tatar'), (b'udm', b'Udmurt'), (b'uk', b'Ukrainian'), (b'ur', b'Urdu'), (b'vi', b'Vietnamese'), (b'zh-cn', b'Simplified Chinese'), (b'zh-hans', b'Simplified Chinese'), (b'zh-hant', b'Traditional Chinese'), (b'zh-tw', b'Traditional Chinese')])),
                ('show_signatures', models.BooleanField(default=True, verbose_name='Show signatures')),
                ('post_count', models.IntegerField(default=0, verbose_name='Post count', blank=True)),
                ('avatar', models.ImageField(upload_to=pybb.util.FilePathGenerator(to=b'pybb/avatar'), null=True, verbose_name='Avatar', blank=True)),
                ('autosubscribe', models.BooleanField(default=True, help_text='Automatically subscribe to topics that you answer', verbose_name='Automatically subscribe')),
                ('about_me', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(500)])),
                ('rendered_about_me', models.TextField(null=True, editable=False)),
                ('main_character', models.CharField(default=b'', max_length=12, null=True, blank=True)),
                ('armory_link', models.CharField(default=b'', max_length=100, null=True, blank=True)),
                ('char_class', models.CharField(default=b'', max_length=15, null=True, blank=True)),
                ('over_18', models.CharField(default=b'', max_length=4, null=True, blank=True)),
                ('char_spec', models.CharField(default=b'', max_length=15, null=True, blank=True)),
                ('recent_parses', models.TextField(default=b'', null=True, blank=True, validators=[django.core.validators.MaxLengthValidator(500)])),
                ('computer_specs', models.TextField(default=b'', null=True, blank=True, validators=[django.core.validators.MaxLengthValidator(1000)])),
                ('screenshot', models.TextField(default=b'', max_length=200, null=True, blank=True)),
                ('addons', models.TextField(default=b'', null=True, blank=True, validators=[django.core.validators.MaxLengthValidator(1000)])),
                ('experience', models.TextField(default=b'', null=True, blank=True, validators=[django.core.validators.MaxLengthValidator(1000)])),
                ('how_did_you_hear', models.TextField(default=b'', null=True, blank=True, validators=[django.core.validators.MaxLengthValidator(500)])),
                ('authenticator', models.CharField(default=b'', max_length=5, null=True, blank=True)),
                ('submitted_app', models.NullBooleanField(default=False)),
                ('previous_guild', models.TextField(default=b'', null=True, blank=True, validators=[django.core.validators.MaxLengthValidator(500)])),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'permissions': (('block_users', 'Can block any user'),),
            },
            bases=(models.Model,),
        ),
    ]
