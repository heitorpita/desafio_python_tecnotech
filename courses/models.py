from django.db import models

class Course(models.Model):
    STATUS_CHOICES = (
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo')
            )


    nome = models.CharField(max_length=100)
    carga_horaria = models.PositiveIntegerField()
    valor_inscricao = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ativo')
    
    def __str__(self):
        return self.nome

