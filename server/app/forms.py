from django import forms
from .models import Application

class DeployForm(forms.ModelForm):
    class Meta:
	model = Application
        fields = ["name", "description", "repo", "path"]
