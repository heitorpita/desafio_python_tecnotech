from django.shortcuts import render, redirect, get_object_or_404
from .models import Enrollment
from students.models import Student
from courses.models import Course
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EnrollmentSerializer
from django.db.models import Sum, Case, When, DecimalField


#html


def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'enrollments/list.html', {'enrollments': enrollments})

def enrollment_create(request):
    if request.method == 'POST':
        Enrollment.objects.create(
            aluno_id=request.POST.get('aluno'),
            curso_id=request.POST.get('curso'),
            
            status_pagamento='PENDENTE' 
        )
        return redirect('enrollment_list')
    
    alunos = Student.objects.all()
    cursos = Course.objects.all()
    return render(request, 'enrollments/create.html', {'alunos': alunos, 'cursos': cursos})

def enrollment_delete(request, id):
    enrollment = get_object_or_404(Enrollment, id=id)
    enrollment.delete()
    return redirect('enrollment_list')

def general_dashboard(request):
    total_alunos = Student.objects.count()
    total_cursos = Course.objects.count()
    cursos_ativos = Course.objects.filter(status=True).count() 
    
    total_matriculas = Enrollment.objects.count()
    
    
    pagas = Enrollment.objects.filter(status_pagamento='PAGO').count()
    pendentes = Enrollment.objects.filter(status_pagamento='PENDENTE').count()
    
    context = {
        'total_alunos': total_alunos,
        'total_cursos': total_cursos,
        'cursos_ativos': cursos_ativos,
        'total_matriculas': total_matriculas,
        'pagas': pagas,
        'pendentes': pendentes,
    }
    return render(request, 'enrollments/dashboard.html', context)

def financial_dashboard(request):
    students_with_totals = Student.objects.annotate(
        total_devido=Sum(
            Case(
                
                When(enrollment__status_pagamento='PENDENTE', then='enrollment__curso__valor_inscricao'),
                default=0,
                output_field=DecimalField()
            )
        ),
        total_pago=Sum(
            Case(
                
                When(enrollment__status_pagamento='PAGO', then='enrollment__curso__valor_inscricao'),
                default=0,
                output_field=DecimalField()
            )
        )
    )
    return render(request, 'enrollments/financeiro.html', {'students': students_with_totals})

def student_history(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    enrollments = Enrollment.objects.filter(aluno=student).select_related('curso')
    
    total_cursos = enrollments.count()
   
    total_investido = sum(e.curso.valor_inscricao for e in enrollments if e.status_pagamento == 'PAGO')
    total_pendente = sum(e.curso.valor_inscricao for e in enrollments if e.status_pagamento == 'PENDENTE')
    
    context = {
        'student': student,
        'enrollments': enrollments,
        'total_cursos': total_cursos,
        'total_investido': total_investido,
        'total_pendente': total_pendente
    }
    return render(request, 'enrollments/relatorio_aluno.html', context)


#api

class EnrollmentListCreateAPI(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class EnrollmentRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class StudentEnrollmentsAPI(generics.ListAPIView):
    serializer_class = EnrollmentSerializer
    def get_queryset(self):
        student_id = self.kwargs['student_id']
        return Enrollment.objects.filter(aluno_id=student_id)

class MarkAsPaidAPI(APIView):
    def patch(self, request, pk):
        enrollment = get_object_or_404(Enrollment, pk=pk)
        enrollment.status_pagamento = 'PAGO'
        enrollment.save()
        return Response(
            {"message": "Matrícula marcada como PAGO com sucesso!", "status": enrollment.status_pagamento}, 
            status=status.HTTP_200_OK
        )

class FinancialReportAPI(APIView):
    def get(self, request):
        report = Student.objects.annotate(
            total_devido=Sum(
                Case(
                    When(enrollment__status_pagamento='PENDENTE', then='enrollment__curso__valor_inscricao'),
                    default=0,
                    output_field=DecimalField()
                )
            ),
            total_pago=Sum(
                Case(
                    When(enrollment__status_pagamento='PAGO', then='enrollment__curso__valor_inscricao'),
                    default=0,
                    output_field=DecimalField()
                )
            )
        ).values('id', 'nome', 'cpf', 'total_devido', 'total_pago')

        data = []
        for item in report:
            data.append({
                "aluno": item['nome'],
                "cpf": item['cpf'],
                "total_devido": item['total_devido'] or 0.00,
                "total_pago": item['total_pago'] or 0.00
            })
        return Response(data)

class GlobalFinanceAPI(APIView):
    def get(self, request):
        total_pendente = Enrollment.objects.filter(status_pagamento='PENDENTE').aggregate(
            total=Sum('curso__valor_inscricao')
        )['total'] or 0

        total_arrecadado = Enrollment.objects.filter(status_pagamento='PAGO').aggregate(
            total=Sum('curso__valor_inscricao')
        )['total'] or 0

        return Response({
            "total_pendente": total_pendente,
            "total_arrecadado": total_arrecadado,
            "moeda": "BRL"
        })
