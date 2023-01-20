from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Neta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("name",)


class CustomUserChangeForm(UserChangeForm):
    class Neta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields
