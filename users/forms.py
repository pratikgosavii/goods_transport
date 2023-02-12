from django import forms
from .models import *



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'type': 'password'
    }))


class registerForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'type': 'password'
    }))

    class Meta:
        model = User
        fields = ["username", "password1", "is_active", "company"]


        widgets = {
            'company': forms.Select(attrs={
                'class': 'form-control', 'id': 'company_goods', 'required' : 'True'
            }),

        }
    
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(registerForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user