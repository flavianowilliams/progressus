from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from chamadas.forms import ChamadaFormCreate, ChamadaFormUpdate
from pages.forms import NoticiaFormCreate, NoticiaFormUpdate
from .models import CadastroChamada, CadastroProfile, CadastroNoticia
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

# perfis

@login_required
@user_passes_test(lambda u:u.is_superuser, login_url='users:login')
def perfis_list_view(request):

    template_name = 'cadastros/profiles_list.html'

    object_list = CadastroProfile.objects.all()

    context = {'object_list': object_list}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u:u.is_superuser, login_url='users:login')
def perfis_delete_view(request, pk):

    template_name = 'cadastros/forms_delete.html'

    object = get_object_or_404(User, pk = pk)

    if request.method == 'POST':
        object.delete()
        return HttpResponseRedirect(reverse_lazy('cadastros:profiles_list'))

    context = {'object': object}

    return render(request, template_name, context)

# chamadas

@login_required
@user_passes_test(lambda u:u.is_superuser, login_url='users:login')
def chamadas_create_view(request):

    template_name = 'cadastros/forms_upload.html'

    if request.method == 'POST':
        form = ChamadaFormCreate(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            CadastroChamada.objects.create(chamada = form.instance)
            return HttpResponseRedirect(reverse_lazy('cadastros:chamadas_list'))
    else:
        form = ChamadaFormCreate

    context = {'titulo': 'Novo cadastro de chamada', 'botao': 'Inscrever' ,'form': form}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u:u.is_superuser, login_url='users:login')
def chamadas_list_view(request):

    template_name = 'cadastros/chamadas_list.html'

    object_list = CadastroChamada.objects.all()

    context = {'object_list': object_list}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u:u.is_superuser, login_url='users:login')
def chamada_update_view(request, pk):

    template_name = 'cadastros/forms_upload.html'

    object = get_object_or_404(CadastroChamada, pk = pk)

    if request.method == 'POST':
        form = ChamadaFormUpdate(request.POST, request.FILES, instance=object.chamada)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('cadastros:chamadas_list'))
    else:
        form = ChamadaFormUpdate(instance=object.chamada)

    context = {'titulo': 'Edição de cadastro de chamada', 'botao': 'Salvar', 'form': form}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u:u.is_superuser, login_url='users:login')
def chamada_delete_view(request, pk):

    template_name = 'cadastros/forms_delete.html'

    object = get_object_or_404(CadastroChamada, pk = pk)

    if request.method == 'POST':
        object.chamada.delete()
        return HttpResponseRedirect(reverse_lazy('cadastros:chamadas_list'))

    context = {'object': object}

    return render(request, template_name, context)

# Notícias

@login_required
@user_passes_test(lambda u:u.is_superuser, login_url='users:login')
def noticia_create_view(request):

    template_name = 'cadastros/forms_upload.html'

    if request.method == 'POST':
        form = NoticiaFormCreate(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            CadastroNoticia.objects.create(noticia = form.instance)
            return HttpResponseRedirect(reverse_lazy('cadastros:noticias_list'))
    else:
        form = NoticiaFormCreate

    context = {'titulo': 'Novo cadastro de chamada', 'botao': 'Inscrever' ,'form': form}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u:u.is_superuser, login_url='users:login')
def noticia_list_view(request):

    template_name = 'cadastros/noticias_list.html'

    object_list = CadastroNoticia.objects.all()

    context = {'object_list': object_list}

    return render(request, template_name, context)

def noticia_update_view(request, pk):

    template_name = 'cadastros/forms_upload.html'

    object = get_object_or_404(CadastroNoticia, pk = pk)

    if request.method == 'POST':
        form = NoticiaFormUpdate(request.POST, request.FILES, instance=object.noticia)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('cadastros:noticias_list'))
    else:
        form = NoticiaFormUpdate(instance=object.noticia)

    context = {'titulo': 'Edição de cadastro de chamada', 'botao': 'Salvar', 'form': form}

    return render(request, template_name, context)

def noticia_delete_view(request, pk):

    template_name = 'cadastros/forms_delete.html'

    object = get_object_or_404(CadastroNoticia, pk = pk)

    if request.method == 'POST':
        object.noticia.delete()
        return HttpResponseRedirect(reverse_lazy('cadastros:noticias_list'))

    context = {'object': object}

    return render(request, template_name, context)