from django import forms
from django.forms import fields
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


from . import models

class CreatePersonForm(forms.ModelForm):
    class Meta:
        model = models.Person
        fields =  '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Me'))

        for field in self.fields.values():
            field.required = False