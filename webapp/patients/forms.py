from .models import Patients
from django.forms import ModelForm


class PatientsForm(ModelForm):
    class Meta:
        model = Patients
        fields = "__all__"
