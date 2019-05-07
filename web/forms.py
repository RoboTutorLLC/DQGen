from django import forms
from web.models import *


class RequestForm(forms.Form):
    input_file = forms.FileField(label='Input File:', widget=forms.FileInput())
    conf_file = forms.FileField(label='Configuration File:', widget=forms.FileInput())
    email = forms.EmailField(max_length=64, label='Email Address:', widget=forms.TextInput(
                                                    attrs={'class': 'form-control',
                                                           'name': 'email',
                                                           'placeholder': 'Email'}))
    def clean(self):
        cleaned_data = super(RequestForm, self).clean()
        email = self.cleaned_data.get('email')
        return cleaned_data