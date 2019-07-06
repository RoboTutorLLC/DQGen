from django import forms
from django.core.validators import FileExtensionValidator
from web.models import *


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = [
            'input_file',
            'email',
            'max_context_lines'
        ]
        # widgets = {
        #     'input_file': forms.FileInput(),
        #     'email': forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #             'name': 'email',
        #             'placeholder': 'Email'
        #         }
        #     )
        # }



# class RequestForm(forms.ModelForm):
#     input_file = forms.FileField(
#         label='Input File', 
#         widget=forms.FileInput(),
#         validators=[FileExtensionValidator(allowed_extensions=(['txt', 'zip']))]
#     )
#     conf_file = forms.FileField(
#         label='Configuration File',
#         widget=forms.FileInput()
#     )
#     email = forms.EmailField(
#         max_length=64,
#         label='Email Address',
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'name': 'email',
    #             'placeholder': 'Email'
    #         }
    #     )
    # )
#     def clean(self):
#         cleaned_data = super(RequestForm, self).clean()
#         # email = self.cleaned_data.get('email')
#         return cleaned_data