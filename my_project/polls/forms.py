from django import forms

from .models import Choice


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ["choice_text"]


class RawChoiceForm(forms.Form):
    text = forms.CharField()
