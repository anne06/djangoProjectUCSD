from django import forms
from .models import UserWebsite


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = UserWebsite
        fields = ["first_name", "last_name", "email", "password"]

    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(NewsletterForm, self).clean()
        return cleaned_data
