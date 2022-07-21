from venv import create
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from chamadas.forms import ChamadaFormCreate, ChamadaFormUpdate
from chamadas.models import Chamada
from .models import CadastroChamada, CadastroProfile
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