from allauth.account.forms import SignupForm
from django import forms
from django.shortcuts import get_object_or_404
from invites.models import Invite
from django.forms import ValidationError


class CustomSignupForm(SignupForm):

    invite_code = forms.CharField(max_length=16, label='Invite Code')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        
        placeholders = {
            'email': 'Email',
            'email2': 'Confirm Email',
            'username': 'Username',
            'password1': 'Password',
            'password2': 'Confirm Password',
            'invite_code': 'Invite Code',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        try:
            get_object_or_404(Invite, code=self.cleaned_data['invite_code'])
        except:
            raise ValidationError('Invalid invite code, please try again.')
 
    def save(self, request):
        invite = get_object_or_404(Invite, code=self.cleaned_data['invite_code'])
        user = super(CustomSignupForm, self).save(request)
        user.save()
        invite.delete()
        return user