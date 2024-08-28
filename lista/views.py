
#Buscando a ferramenta que lista os dados no banco de dados(ListView)
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from django.views import View
from django.shortcuts import render, redirect
from .forms import MeuCadastroForm
@login_required
def alunos_list(request):
    return render(request, 'lista/alunos_list.html')

#Dizendo onde encontrar o modelo alunos
from .models import Alunos
##Ferramenta pra redirecionar para uma pagina
from django.urls import reverse_lazy
from .forms import MeuLoginForm

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


##Login
class MeuLoginView(LoginView):
    template_name = 'lista/login.html'
    form_class = MeuLoginForm
    redirect_authenticated_user = True  # Redireciona usuários logados para a página principal
    success_url = reverse_lazy('alunos_list')  # Página para onde o usuário será redirecionado após o login


class MeuCadastroView(View):
    form_class = MeuCadastroForm
    initial = {'key': 'value'}
    template_name = 'lista/cadastro.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireciona para a tela de login após o cadastro

        return render(request, self.template_name, {'form': form})