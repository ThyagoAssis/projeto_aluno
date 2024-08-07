from django.shortcuts import render

#Criar uma função com um paramentro par receber a requisição
def home(request):
    #Os colchetes cria um array (lista), para criar divisao utiliza-se virgula
    #As chaves {} criam um dicionario
    #Aqui temos uma lista de dicionários
    alunos = [
        {"nome": "Marcos Silva", "curso": "PHP", "turma": "2024.5"},
        {"nome": "Maria de Jesus", "curso": "Python", "turma": "2024.3"},
        {"nome": "Joao Alves", "curso": "Informatica basica", "turma": "2024.8"},
        {"nome": "Otaviano Costa", "curso": "Informatica basica", "turma": "2024.4"}
    ]
    return render(request, "minha_lista/minha_lista.html", {"dados": alunos})




def contato(request):
    return render(request, "minha_lista/contato.html")