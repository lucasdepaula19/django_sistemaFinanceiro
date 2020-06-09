from django import forms
from .models import ClassContasReceber

class ClassContasReceberForm(forms.ModelForm):
    class Meta:
        model = ClassContasReceber
        fields = ['descricao']