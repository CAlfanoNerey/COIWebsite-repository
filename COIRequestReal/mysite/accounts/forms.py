from django import forms
#from django.contrib.auth import models
from django.core.validators import MaxValueValidator

from .models import Requester, Recipient
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )
        def save(self, commit = True):
            user = super(RegistrationForm, self).save(commit=False)
            user.first_name = cleaned_data['first_name']
            user.first_name = cleaned_data['last_name']
            user.email = cleaned_data['email']

            if commit:
                user.save()

            return user


class RequesterForm(forms.ModelForm):
    # addresLine1 = forms.CharField(label = 'Address Line 1', max_length=200,)
    # addresLine2 = forms.CharField(required=False)
    # city = forms.CharField(label = 'City', max_length=200,)
    # zip = forms.IntegerField(validators=[MaxValueValidator(99999)])
    # fax = forms.IntegerField(required=False)
    class Meta:
        model = Requester
        exclude = ['user']
        fields = ('__all__')

class RecipientForm(forms.ModelForm):

    class Meta:
        model = Recipient
        exclude = ['user']
        fields = ('__all__') #('user', 'name', 'address_line1', 'address_line2', 'city','state','email', 'zipcode', 'fax')

