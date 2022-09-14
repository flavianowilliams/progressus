from django.shortcuts import render

from chamadas.models import Chamada

# Create your views here.

def HomePageDetail(request):

    template_name = 'pages/index.html'

    chamada = [object for object in Chamada.objects.all() if object.get_status() != 'Encerrado']

    context = {'chamada': chamada}

    return render(request, template_name, context)