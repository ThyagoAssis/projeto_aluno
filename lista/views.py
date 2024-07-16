from django.shortcuts import render

#Criar uma função com um paramentro par receber a requisição
def home(request):
    #Varivel de titulo
    titulo1 = "Lista de Alunos"
    alunos = ["Mateus Silva", "Ronaldo Nazario", "Marina Silva", "Jorge Alves", "Bolsonaro", "Lula"]

    #Para criar um dicionario em python, cria uma variavel com chaves
    lista_alunos = {
        #Informa a variavel titulo1 para o campo "titulo" do dicionario
        "titulo": titulo1,
        "nome": alunos,
    }
    return render(request, "minha_lista/minha_lista.html", lista_alunos)




def contato(request):
    return render(request, "minha_lista/contato.html")