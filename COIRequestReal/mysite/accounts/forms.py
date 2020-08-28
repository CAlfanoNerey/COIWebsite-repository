from django import forms
from django.core.validators import MaxValueValidator

from .models import Requesters, Recipient



class RequesterForm(forms.ModelForm):
    # addresLine1 = forms.CharField(label = 'Address Line 1', max_length=200,)
    # addresLine2 = forms.CharField(required=False)
    # city = forms.CharField(label = 'City', max_length=200,)
    # zip = forms.IntegerField(validators=[MaxValueValidator(99999)])
    # fax = forms.IntegerField(required=False)
    class Meta:
        model = Requesters
        exclude = ['user']
        fields = ('__all__')

class RecipientForm(forms.ModelForm):

    class Meta:
        model = Recipient
        exclude = ['user']
        fields = ('__all__') #('user', 'name', 'address_line1', 'address_line2', 'city','state','email', 'zipcode', 'fax')

