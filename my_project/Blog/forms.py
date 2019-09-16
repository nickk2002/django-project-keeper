from django import forms
import re
from .models import Article
from django.contrib.auth.models import User

class ArticleForm(forms.ModelForm):
    title = forms.CharField()
    article = forms.CharField(widget=forms.Textarea(
        attrs={
            "size": 50,
        }
    ))

    class Meta:
        model = Article
        fields = ["title", "article"]

    def clean_title(self,*args,**kwargs):
        title = self.cleaned_data["title"]
        if len(title) >= 10 and re.search("^[A-Z]",title):
            return title
        else:
            raise forms.ValidationError("Enter a new title! Should have the first letter uppercase and at least 10 characters")

