from django.contrib import admin
from django.urls import path

#Importando nossa função home da nossa view
from lista.views import AlunosListView, AlunosCreateView, AlunosUpdateView, AlunosDeleteView, MeuLoginView, MeuCadastroView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),

    ## com o patch vazio temos a nosssa pagina(rota) principal
    path('', MeuLoginView.as_view(), name='login'),
    path('cadastro/', MeuCadastroView.as_view(), name='cadastro'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('lista/', AlunosListView.as_view(), name='alunos_list'),
    path('cadastro/', AlunosCreateView.as_view(), name='alunos_form'),
    path('edicao/<int:pk>/', AlunosUpdateView.as_view(), name='alunos_edicao'),
    path('delete/<int:pk>/', AlunosDeleteView.as_view(), name='alunos_delete'),

]