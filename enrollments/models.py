from django.db import models
from students.models import Student
from courses.models import Course

class Enrollment(models.Model):
    STATUS_CHOICES = (
    ('pago', 'Pago'),
    ('pendente', 'Pendente')
    )

    aluno = models.ForeignKey(Student, on_delete=models.CASCADE)

    curso = models.ForeignKey(Course, on_delete=models.CASCADE)

    data_matricula = models.DateField(auto_now_add=True)
    status_pagamento = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')

    class Meta:
        unique_together = ('aluno', 'curso')

    def __str__(self):
        return f"{self.aluno.nome} -> {self.curso.nome}"

