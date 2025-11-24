from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from main.models import Task #importa a tabela  que vamos usar
class HomeView(TemplateView):
    template_name = 'home.html'


class TaskList(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tarefas'
    
    # views - urls - template
    
def task_list(request):
    tarefas = Task.objects.all()    #trazendo tudo para a tabela task
    context = {
        "tarefas": tarefas,
        "titulo_pagina": 'Minhas Tarefas'
    }
    return render(request, 'tasks/task_list.html', context)

def task_concluido(request):
    a = 4
    b = 5
    c = a + b

    tarefas = Task.objects.filter(concluida=1)  # trazendo tudo áta tabela task
    context = {
        "tarefas": tarefas,
        "titulo_pagina": 'Minhas tarefas concluidas'
    }
    return render(request, 'tasks/teste.html', context)

def task_nao_concluido(request):
    
    tarefas = Task.objects.filter(concluida=0)  # trazendo tudo áta tabela task
    context = {
        "tarefas": tarefas,
        "titulo_pagina": 'Minhas tarefas nao concluidas'
    }
    return render(request, 'tasks/teste.html', context)