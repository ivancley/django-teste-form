from django.shortcuts import render
from perguntas.models import Pergunta

def homePergunta(request):
    return render(request, 'pergunta/home.html')

def formularioPergunta(request):
    perguntas = Pergunta.objects.all()
    return render(request, 'pergunta/formulario.html', {"perguntas":perguntas})
