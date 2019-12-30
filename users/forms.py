from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age',)


class CustomUserChangeForm(UserChangeForm):

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("the given email is already registered")
        return self.cleaned_data['email']

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
        
        
        



class SignUpForm(forms.ModelForm):
    def clean_email(self):
        if CustomUser.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("the given email is already registered")
        return self.cleaned_data['email']
        
    class Meta:
        model = CustomUser
        fields= ['username', 'password', 'email', 'first_name', 'last_name']
       