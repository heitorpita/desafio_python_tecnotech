from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', { 'students': students })

def student_create(request):
    if request.method == 'POST':
        Student.objects.create(
            nome=request.POST['nome'],
            email=request.POST['email'],
            cpf=request.POST['cpf'],
            data_ingresso=request.POST['data_ingresso']
        )
        return redirect('student_list')

    return render(request, 'students/create.html')
