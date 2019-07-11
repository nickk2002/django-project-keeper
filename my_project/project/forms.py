from django import forms
from django.conf import settings

from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "data", "image"]


