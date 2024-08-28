from django.shortcuts import render

#Buscando a ferramenta que lista os dados no banco de dados(ListView)
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
#Dizendo onde encontrar o modelo alunos
from .models import Alunos
##Ferramenta pra redirecionar para uma pagina
from django.urls import reverse_lazy

#Classe de consulta aos dados
class AlunosListView(ListView):
    model = Alunos

#Criando a classe para cadastro
class AlunosCreateView(CreateView):
    #Informa o modelo a ser usado
    model = Alunos
    #QQuais campos da nossa tabela sera preenchida
    fields = ["nome","curso","turma"]
    #Redireciona para uma pagina
    success_url = reverse_lazy('alunos_list')

#Classe de edição
class AlunosUpdateView(UpdateView):
    model = Alunos
    fields = ["nome", "curso", "turma"]
    template_name = 'lista/alunos_form.html'
    success_url = reverse_lazy('alunos_list')

class AlunosDeleteView(DeleteView):
    model = Alunos
    template_name = 'lista/alunos_delete.html'
    success_url = reverse_lazy('alunos_list')