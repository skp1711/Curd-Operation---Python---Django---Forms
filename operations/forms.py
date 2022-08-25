from django import forms
from django.forms import ModelForm
from .models import Curd


class CurdForm(forms.ModelForm):
    class Meta:
        model = Curd
        fields = "__all__"
