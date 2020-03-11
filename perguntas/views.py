from django.shortcuts import render, redirect
from perguntas.models import Pergunta
from respostas.models import Resposta
from django.forms.models import modelformset_factory, inlineformset_factory


def homePergunta(request):
    return render(request, 'pergunta/home.html')

def formularioPergunta(request):
    #RespostaFormSet = modelformset_factory(Resposta, Pergunta, fields=('resp_texto',), extra=1)
    RespostaFormSet = inlineformset_factory(Resposta, Pergunta, fields=('resp_texto',), extra=1)
    if request.method == "POST":
        formset = RespostaFormSet(request.POST )
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.save()
            return redirect("/feedback")
    else:
        perguntas = Pergunta.objects.all()
        for pergunta in perguntas:
            resp = Resposta()
            resp.pergunta = pergunta
            #resp.save()
            formset = RespostaFormSet(queryset = Resposta.objects.all() )
    return render(request, 'pergunta/formulario.html', {"formset":formset})

def feedback(request):
    respostas = Resposta.objects.all()
    return render(request, "pergunta/feedback.html", {"respostas":respostas})
