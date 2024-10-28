# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    firstname = forms.CharField(max_length=255, label="First Name")
    lastname = forms.CharField(max_length=255, label="Last Name")
    phone_number = forms.CharField(max_length=15, required=False, label="Phone Number")
    email = forms.EmailField(required=True, label="Email")
    address = forms.CharField(widget=forms.Textarea, required=False, label="Address")

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Save profile details in UserProfile
            UserProfile.objects.create(
                user=user,
                firstname=self.cleaned_data['firstname'],
                lastname=self.cleaned_data['lastname'],
                phone_number=self.cleaned_data['phone_number'],
                email=self.cleaned_data['email'],
                address=self.cleaned_data['address']
            )
        return user
