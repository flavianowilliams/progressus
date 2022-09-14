from django.shortcuts import render, get_object_or_404
from chamadas.models import Chamada
from cadastros.models import CadastroNoticia

# Create your views here.

def HomePageDetail(request):

    template_name = 'pages/index.html'

    chamada = [object for object in Chamada.objects.all() if object.get_status() != 'Encerrado']

    noticia = CadastroNoticia.objects.all()

    context = {'chamada': chamada, 'noticia': noticia}

    return render(request, template_name, context)

def noticia_detail_view(request, pk):

    template_name = 'pages/noticia_detail.html'

    object = get_object_or_404(CadastroNoticia, pk = pk)

    context = {'object': object}

    return render(request, template_name, context)

def noticias_list_view(request):

    template_name = 'pages/noticias_list.html'

    object_list = CadastroNoticia.objects.all()

    context = {'object_list': object_list}

    return render(request, template_name, context)
