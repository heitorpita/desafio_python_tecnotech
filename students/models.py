from django.db import models

class Student(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    data_ingresso = models.DateField()

    def __str__(self):
        return self.nome
