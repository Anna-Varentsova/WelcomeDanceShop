from django import forms
from .models import Articles


class AddArtForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Articles
        fields = 'title', 'content', 'content2', 'content3', 'content4', 'photo', 'photo1', 'slug'
        widgets = {
            'title': forms.Textarea(attrs={'placeholder': 'Название статьи', 'cols': 70, 'rows': 2}),
            'content': forms.Textarea(attrs={'placeholder': 'Текст первого абзаца', 'cols': 70, 'rows': 20}),
            'content2': forms.Textarea(attrs={'placeholder': 'Текст второго абзаца', 'cols': 70, 'rows': 20}),
            'content3': forms.Textarea(attrs={'placeholder': 'Текст третьего абзаца', 'cols': 70, 'rows': 20}),
            'content4': forms.Textarea(attrs={'placeholder': 'Текст четвертого абзаца', 'cols': 70, 'rows': 20}),
        }