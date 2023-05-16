from .models import Student
from django.forms import ModelForm

def AddStudent(ModelForm):
    class Meta:
        model = Student
        fields = ['fio', 'group', 'title']

