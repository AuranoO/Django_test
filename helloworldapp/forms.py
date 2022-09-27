from django import forms

from .models import Person


# This form model is based on the person model, so that it takes the good input fields

class FormPerson(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name',)
