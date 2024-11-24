from django import forms
from .models import Examinations


class ExaminationForm(forms.ModelForm):
    class Meta:
        model = Examinations
        fields = "__all__"

