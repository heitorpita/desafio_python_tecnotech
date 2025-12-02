from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from rest_framework import generics
from .serializers import StudentSerializer

#html

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

def student_edit(request, id):
    aluno = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        aluno.nome = request.POST['nome']
        aluno.email = request.POST['email']
        aluno.cpf = request.POST['cpf']
        aluno.data_ingresso = request.POST['data_ingresso']
        aluno.save()
        return redirect('student_list')

    return render(request, 'students/edit.html', {'aluno': aluno})

def student_delete(request, id):
    aluno = get_object_or_404(Student, id=id)
    aluno.delete()
    return redirect('student_list')

#api

class StudentListCreateAPI(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer