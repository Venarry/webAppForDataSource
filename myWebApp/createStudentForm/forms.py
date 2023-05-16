from main.models import Student
from django.forms import ModelForm, TextInput, Textarea


class AddStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['fio', 'group', 'title']

        widgets = {
            "fio": TextInput(attrs={
                'class': 'form-control',
            }),

            "group": TextInput(attrs={
                'class': 'form-control',
            }),

            "title": Textarea(attrs={
                'class': 'form-control',
            }),
        }
