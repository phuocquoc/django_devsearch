from django.forms import ModelForm
from django import forms
from .models import Project


class Project_Form(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(Project_Form, self).__init__(*args, **kwargs)
        for name, fields in self.fields.items():
            fields.widget.attrs.update({'class': 'input'})
