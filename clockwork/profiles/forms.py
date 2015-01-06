from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Layout, Fieldset, Submit, Button,
                                 HTML, Field)
from crispy_forms.bootstrap import FormActions

from .models import UserProfile


# Create the form class.
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    about_me = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Field('first_name'),
            Field('last_name'),
            HTML('<hr>'),
            Field('about_me'),
            HTML('<br>'),
            FormActions(
                Submit('save', 'Save changes',
                       epiceditor_save_button="true"),
                Button('cancel', 'Cancel',
                       onclick="window.location='/profile/'")
            ),
        )

    def save(self, *args, **kwargs):
        profile = super(UserProfileForm, self).save(*args, **kwargs)
        profile.user.first_name = self.cleaned_data['first_name']
        profile.user.last_name = self.cleaned_data['last_name']
        profile.user.profile.submitted_app = True
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

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',
                   'about_me',
                   'avatar',
                   'post_count',
                   'time_zone',
                   'language',
                   'show_signatures',
                   'autosubscribe',
                   'signature',
                   'signature_html',)
        fields = ['main_character',
                  'armory_link',
                  'char_race',
                  'char_class',
                  'age',
                  'char_spec',
                  'recent_parses',
                  'computer_specs',
                  'screenshot',
                  'experience',
                  'how_did_you_hear',
                  'authenticator',
                  'addons',
                  'submitted_app',]
                  

    race_choices = ['Draenei',
                    'Dwarf',
                    'Gnome',
                    'Human',
                    'Night Elf',
                    'Pandaren',
                    'Worgen',]

    class_choices = ['Death Knight',
                     'Hunter',
                     'Mage',
                     'Monk',
                     'Paladin',
                     'Priest',
                     'Shaman',
                     'Warrior',]

    auth_choices = ['Yes', 'No',]

    main_character = forms.CharField(required=True)
    armory_link = forms.URLField(required=True)
    char_race = forms.ChoiceField(required=True, choices=[(x, x) for x in race_choices])
    char_class = forms.ChoiceField(required=True, choices=[(x, x) for x in class_choices])
    age = forms.CharField(required=True)
    char_spec = forms.CharField(required=True)
    recent_parses = forms.CharField(required=True, widget=forms.Textarea)
    computer_specs = forms.CharField(required=True, widget=forms.Textarea)
    screenshot = forms.CharField(required=True)
    experience = forms.CharField(required=True, widget=forms.Textarea)
    how_did_you_hear = forms.CharField(required=True, widget=forms.Textarea)
    authenticator = forms.CharField(required=True)
    submitted_app = forms.BooleanField(required=False)
    
    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        initial['submitted_app'] = 'True'
        kwargs['initial'] = initial
        super(ApplicationForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.layout = Layout(
            Field('main_character'),
            HTML('<hr>'),
            Field('armory_link'),
            HTML('<hr>'),
            Field('char_race'),
            HTML('<hr>'),
            Field('char_class'),
            HTML('<hr>'),
            Field('age'),
            HTML('<hr>'),
            Field('char_spec'),
            HTML('<hr>'),
            Field('recent_parses'),
            HTML('<hr>'),
            Field('computer_specs'),
            HTML('<hr>'),
            Field('screenshot'),
            HTML('<hr>'),
            Field('addons'),
            HTML('<hr>'),
            Field('experience'),
            HTML('<hr>'),
            Field('how_did_you_hear'),
            HTML('<hr>'),
            Field('authenticator'),
            Field('submitted_app', type="hidden"),
            HTML('<br>'),
            FormActions(
                Submit('save', 'Submit Application'),
                Button('cancel', 'Cancel', onclick="window.location='/'"),
            ),
            HTML('<br><br>'),
        )
        
        self.fields['main_character'].label = "Main Character"
        self.fields['armory_link'].label = "Link your Armory"
        self.fields['char_race'].label = "Character Race"
        self.fields['char_class'].label = "Character Class"
        self.fields['age'].label = "How old are you?"
        self.fields['char_spec'].label = "What is your primary raiding spec?"
        self.fields['recent_parses'].label = "Link some recent parses"
        self.fields['computer_specs'].label = "List your computer specs"
        self.fields['screenshot'].label = "Link a screenshot of your UI during combat"
        self.fields['addons'].label = "What addons do you use?"
        self.fields['experience'].label = "List your previous raiding experience"
        self.fields['how_did_you_hear'].label = "How did you hear about Clockwork and why do you want to be a part of it?"
        self.fields['authenticator'].label = "Is your account secure with an authenticator?"
        self.fields['submitted_app'].label = "Check this box if "
        
    def save(self, *args, **kwargs):
        profile = super(ApplicationForm, self).save(*args, **kwargs)
        print profile.user.username
        profile.user.main_character = self.cleaned_data['main_character']
        profile.user.armory_link = self.cleaned_data['main_character']
        profile.user.char_race = self.cleaned_data['char_race']
        profile.user.char_class = self.cleaned_data['char_race']
        profile.user.age = self.cleaned_data['age']
        profile.user.char_spec = self.cleaned_data['char_spec']
        profile.user.recent_parses = self.cleaned_data['recent_parses']
        profile.user.computer_specs = self.cleaned_data['computer_specs']
        profile.user.screenshot = self.cleaned_data['screenshot']
        profile.user.addons = self.cleaned_data['addons']
        profile.user.experience = self.cleaned_data['experience']
        profile.user.how_did_you_hear = self.cleaned_data['how_did_you_hear']
        profile.user.authenticator = self.cleaned_data['authenticator']
        profile.user.submitted_app = self.cleaned_data['submitted_app']
        profile.user.save(*args, **kwargs)

        
        print u"{}'s profile saved".format(profile.user.username)
        print "submitted_app = {}".format(profile.user.submitted_app)
        return profile
