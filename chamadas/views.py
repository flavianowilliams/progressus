from multiprocessing import context
from django.shortcuts import render

from chamadas.models import Chamada

# Create your views here.

def abertas_list_view(request):

    template_name = 'chamadas/chamadas_abertas.html'

    object_list = [object for object in Chamada.objects.all() if object.get_status() == 'Aberto']

    context = {'object_list': object_list}

    return render(request, template_name, context)

def andamento_list_view(request):

    template_name = 'chamadas/chamadas_andamento.html'

    object_list = [object for object in Chamada.objects.all() if object.get_status() == 'Em andamento']

    context = {'object_list': object_list}

    return render(request, template_name, context)

def encerradas_list_view(request):

    template_name = 'chamadas/chamadas_encerradas.html'

    object_list = [object for object in Chamada.objects.all() if object.get_status() == 'Encerrado']

    context = {'object_list': object_list}

    return render(request, template_name, context)
