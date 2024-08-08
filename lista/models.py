from django.db import models

# Create your models here.
#Criado nosso modelo de banco de dados Atraves de classes
class Alunos(models.Model):
    #Criando os campos da tabela
    nome = models.CharField(max_length=30,null=False,blank=False)
    curso = models.CharField(max_length=30,null=False,blank=False)
    turma = models.CharField(max_length=10,null=False,blank=False)