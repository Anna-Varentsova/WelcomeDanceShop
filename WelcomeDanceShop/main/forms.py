from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EmailPostForm(forms.Form):
    name = forms.CharField(label='Тема', max_length=25)
    email = forms.EmailField(label='Ваш e-mail')
    comments = forms.CharField(label='Сообщение', required=False, widget=forms.Textarea)


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Эл. почта', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Пароль ещё раз', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')