from django import forms
from .models import Cadastro

class Itemform(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = '__all__'