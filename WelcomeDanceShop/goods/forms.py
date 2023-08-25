from django import forms

from goods.models import Gender


class SearchGoodForm(forms.Form):
    title = forms.CharField(label='Товар', widget=forms.TextInput(attrs=
                                                                 {'class': 'myfield',
                                                                  'placeholder': 'Поиск...',}), required=False)
    gender = forms.ModelChoiceField(label='Пол', queryset=Gender.objects.all(), empty_label='', required=False)