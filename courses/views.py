from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from rest_framework import generics
from .serializers import CourseSerializer
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection

#html

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/list.html', {'courses': courses})

def course_create(request):
    if request.method == 'POST':
        Course.objects.create(
            nome=request.POST.get('nome'),
            carga_horaria=request.POST.get('carga_horaria'),
            valor_inscricao=request.POST.get('valor_inscricao'),
            status=request.POST.get('status') == 'on'
        )
        return redirect('course_list')
    return render(request, 'courses/create.html')

def course_edit(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        course.nome = request.POST.get('nome')
        course.carga_horaria = request.POST.get('carga_horaria')
        course.valor_inscricao = request.POST.get('valor_inscricao')
        course.status = request.POST.get('status') == 'on'
        course.save()
        return redirect('course_list')
    return render(request, 'courses/edit.html', {'course': course})

def course_delete(request, id):
    course = get_object_or_404(Course, id=id)
    course.delete()
    return redirect('course_list')

#api

class CourseListCreateAPI(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseStatsAPI(APIView):

    def get(self, request):

        
        stats = Course.objects.annotate(
            total_matriculas=Count('enrollment') 
        ).values('id', 'nome', 'total_matriculas')

        return Response(stats)
    

class SQLRawReportAPI(APIView):

    def get(self, request):

        sql = """
            SELECT 
                c.nome,
                COUNT(e.id) as total_alunos,
                COALESCE(SUM(c.valor_inscricao), 0) as receita_estimada
            FROM 
                courses_course c
            LEFT JOIN 
                enrollments_enrollment e ON c.id = e.curso_id
            GROUP BY 
                c.nome
            ORDER BY 
                receita_estimada DESC;
        """

        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()

        data = [
            {
                "curso": row[0],
                "total_alunos": row[1],
                "receita_estimada": row[2]
            }
            for row in rows
        ]

        return Response(data)