from django.urls import path
from main.views import TaskList
from . import views

urlpatterns = [
    path("", TaskList.as_view(), name='task_list'),
    path('funcao/', views.task_list, name='task_list_funcao'),
    path('concluido/', views.task_concluido, name='task_concluido'),
    path('nao concluidas', views.task_nao_concluido, name='task_nao_concluida')
]