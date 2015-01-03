from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Layout, Fieldset, Submit, Button,
                                                                  HTML, Field)
from crispy_forms.bootstrap import FormActions

from .models import UserProfile

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

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
    armory_link = forms.CharField(required=True)
    char_race = forms.ChoiceField(required=True, choices=race_choices)
    char_class = forms.ChoiceField(required=True, choices=class_choices)
    age = forms.IntegerField(required=True)
    char_spec = forms.CharField(required=True)
    recent_parses = forms.CharField(required=True)
    computer_specs = forms.CharField(required=True)
    screenshot = forms.CharField(required=True)
    experience = forms.CharField(required=True)
    how_did_you_hear = forms.CharField(required=True)
    authenticator_check = forms.ChoiceField(required=True, choices=auth_choices, widget=forms.RadioSelect())

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Field('main_character'),
            Field('armory_link'),
            Field('char_race'),
            Field('char_class'),
            Field('age'),
            Field('char_spec')
            Field('recent_parses'),
            Field('computer_specs'),
            Field('screenshot'),
            Field('experience'),
            Field('how_did_you_hear'),
            Field('authenticator_check'),
            FormActions(
                Submit('save', 'Submit Application'),
                Button('cancel', 'Cancel', onclick="window.location='/profile'")
            ),
        )
        
        def save(self, *args, **kwargs):
            profile = super(ApplicationForm, self).save(*args, **kwargs)
            profile.user.main_character = self.cleaned_data['main_character']
            profile.user.armory_link = self.cleaned_data['main_character']
            profile.user.char_race = self.cleaned_data['char_race']
            profile.user.char_class = self.cleaned_data['char_race']
            profile.user.age = self.cleaned_data['age']
            profile.user.char_spec = self.cleaned_data['char_spec']
            profile.user.recent_parses = self.cleaned_data['recent_parses']
            profile.user.computer_specs = self.cleaned_data['computer_specs']
            profile.user.screenshot = self.cleaned_data['screenshot']
            profile.user.experience = self.cleaned_data['experience']
            profile.user.how_did_you_hear = self.cleaned_data['how_did_you_hear']
            profile.user.authenticator = self.cleaned_data['authenticator_check']

            print u"{}'s profile saved".format(profile.user.username)
            return profile
            
