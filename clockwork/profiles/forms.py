from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils import timezone

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Layout, Fieldset, Submit, Button,
                                 HTML, Field)
from crispy_forms.bootstrap import FormActions

from .models import UserProfile, Application

import datetime

# Create the form class.
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
        fields = ['about_me','avatar', 'signature']

    about_me = forms.CharField(required=False, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.layout = Layout(
            Field('about_me'),
            HTML('<br>'),
            Field('avatar'),
            HTML('<br>'),
            Field('signature'),
            HTML('<br>'),
            FormActions(
                Submit('save', 'Save changes'),
            ),
            HTML('<br><br>'),
        )

        self.fields['avatar'].label = "Forum Avatar"
        self.fields['signature'].label = "Forum Signature"

    def save(self, *args, **kwargs):
        profile = super(UserProfileForm, self).save(*args, **kwargs)
        profile.user.about_me = self.cleaned_data['about_me']
        profile.user.avatar = self.cleaned_data['avatar']
        profile.user.signature = self.cleaned_data['signature']
        profile.user.save(*args, **kwargs)
        print u"{}'s profile saved".format(profile.user.username)
        return profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, request=None, **kwargs):
        self.request = request

        super(LoginForm, self).__init__(**kwargs)

        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Fieldset(
                'Login',
                'username',
                'password',
            ),
            FormActions(
                Submit('login', 'Login'),
            ),
        )

    def clean(self):
        """Make sure the username/password combos match"""
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data['username']
        password = cleaned_data['password']

        error_message = "Username/password combination does not match"

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError(error_message)

        # Check the password
        if not user.check_password(password):
            raise forms.ValidationError(error_message)

        return cleaned_data

    def get_user(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        return authenticate(username=username, password=password)

default_submit_time = datetime.datetime(2000, 1, 1, 6, 0, tzinfo=timezone.utc)
    
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        
        fields = ['main_character',
                  'armory_link',
                  'char_class',
                  'over_18',
                  'char_spec',
                  'recent_parses',
                  'computer_specs',
                  'screenshot',
                  'experience',
                  'how_did_you_hear',
                  'authenticator',
                  'addons',
                  'previous_guild',
                  'battle_tag',]
                  
    class_choices = ['Death Knight',
                     'Hunter',
                     'Mage',
                     'Monk',
                     'Paladin',
                     'Priest',
                     'Shaman',
                     'Warrior',
                     'Warlock',
                     'Druid',
                     'Rogue',]

    auth_choices = ['Yes', 'No',]

    main_character = forms.CharField(required=True)
    armory_link = forms.URLField(required=True)
    char_class = forms.ChoiceField(required=True, choices=[(x, x) for x in class_choices])
    over_18 = forms.ChoiceField(required=True, choices=[(x,x) for x in auth_choices])
    char_spec = forms.CharField(required=True)
    recent_parses = forms.CharField(required=True, widget=forms.Textarea)
    computer_specs = forms.CharField(required=True, widget=forms.Textarea)
    screenshot = forms.CharField(required=True, widget=forms.Textarea)
    experience = forms.CharField(required=True, widget=forms.Textarea)
    how_did_you_hear = forms.CharField(required=True, widget=forms.Textarea)
    authenticator = forms.ChoiceField(required=True, choices=[(x,x) for x in auth_choices])
    previous_guild = forms.CharField(required=True, widget=forms.Textarea)
    addons = forms.CharField(required=True, widget=forms.Textarea)
    battle_tag = forms.CharField(required=True)
    
    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.layout = Layout(
            Field('main_character'),
            HTML('<hr>'),
            Field('char_class'),
            HTML('<hr>'),
            Field('char_spec'),
            HTML('<hr>'),
            Field('armory_link'),
            HTML('<hr>'),
            Field('recent_parses'),
            HTML('<hr>'),
            Field('screenshot'),
            HTML('<hr>'),
            Field('addons'),
            HTML('<hr>'),
            Field('computer_specs'),
            HTML('<hr>'),
            Field('authenticator'),
            HTML('<hr>'),
            Field('over_18'),
            HTML('<hr>'),
            Field('how_did_you_hear'),
            HTML('<hr>'),
            Field('previous_guild'),
            HTML('<hr>'),
            Field('experience'),
            HTML('<br>'),
            Field('battle_tag'),
            HTML('<br>'),
            FormActions(
                Submit('save', 'Submit Application'),
                Button('cancel', 'Cancel', onclick="window.location='/'"),
            ),
            HTML('<br><br>'),
        )
        
        self.fields['main_character'].label = "Main Character"
        self.fields['armory_link'].label = "Link your Armory"
        self.fields['char_class'].label = "Character Class"
        self.fields['over_18'].label = "Are you 18 or older?"
        self.fields['char_spec'].label = "What is your primary raiding specialization?"
        self.fields['recent_parses'].label = "Link some recent parses (Mandatory, application will be ignored until they are provided)"
        self.fields['computer_specs'].label = "List your computer specs"
        self.fields['screenshot'].label = "Link a screenshot of your UI during combat"
        self.fields['addons'].label = "What addons do you use?"
        self.fields['experience'].label = "Tell us about your previous raiding history.  What content did you clear and with which guilds?"
        self.fields['how_did_you_hear'].label = "How did you hear about Clockwork and why do you want to join us?"
        self.fields['previous_guild'].label = "Tell us about your previous guild.  What makes us a more attractive option?"
        self.fields['authenticator'].label = "Do you use an authenticator?"
        self.fields['battle_tag'].label = "Provide us your battle tag so we may contact you about your application."
        
    def save(self, *args, **kwargs):
        app = super(ApplicationForm, self).save(*args, **kwargs)
        
        app.user.application.main_character = self.cleaned_data['main_character']
        app.user.application.armory_link = self.cleaned_data['armory_link']
        app.user.application.over_18 = self.cleaned_data['over_18']
        app.user.application.char_spec = self.cleaned_data['char_spec']
        app.user.application.recent_parses = self.cleaned_data['recent_parses']
        app.user.application.computer_specs = self.cleaned_data['computer_specs']
        app.user.application.screenshot = self.cleaned_data['screenshot']
        app.user.application.addons = self.cleaned_data['addons']
        app.user.application.experience = self.cleaned_data['experience']
        app.user.application.how_did_you_hear = self.cleaned_data['how_did_you_hear']
        app.user.application.authenticator = self.cleaned_data['authenticator']
        app.user.application.previous_guild = self.cleaned_data['previous_guild']
        app.user.application.battle_tag = self.cleaned_data['battle_tag']
        
        # Only update updated if submitted != default
        if app.user.application.submitted != default_submit_time:
            app.user.application.updated = datetime.datetime.now()
        else:
            app.user.application.submitted = datetime.datetime.now()


        
        app.user.application.save(*args, **kwargs)
        app.user.profile.submitted_app = True
        app.user.profile.save(*args, **kwargs)

        print u"{}'s app saved".format(app.user.username)

        return app
