from django.shortcuts import render, redirect
from .forms import AddStudentForm


def create(request):
    error = ''
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "ээээ"

    form = AddStudentForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/CreateStudentForm.html', data)
