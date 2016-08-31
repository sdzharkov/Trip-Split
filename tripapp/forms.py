from django import forms
from django.contrib.auth.models import User
class RegForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    check_pass = forms.CharField(label='Re-type Password', widget=forms.PasswordInput())
    def clean(self):
        cleaned_data = super(RegForm, self).clean()
        password = cleaned_data.get('password')
        check_pass = cleaned_data.get('check_pass')
        if password != check_pass:
            raise forms.ValidationError('Passwords do not match.')
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError('This Username is taken.')
        return cleaned_data




class googleForm(forms.Form):
    source = forms.CharField(label='source', max_length=100)
    dest = forms.CharField(label='dest', max_length=100)
