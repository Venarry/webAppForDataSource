from main.models import Student
from django.forms import ModelForm

class AddStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['fio', 'group', 'title']
