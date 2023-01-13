from django.shortcuts import render

from django.shortcuts import render

# Create your views here.


def novo_servico(request):
    return render(request, 'novo_servico.html')
