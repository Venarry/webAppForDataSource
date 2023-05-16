from django.shortcuts import render
from .models import Student


def start_site(request):
    students = Student.objects.all()
    return render(request, 'main/index.html', {'students': students})
