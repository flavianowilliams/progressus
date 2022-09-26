from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from chamadas.forms import ChamadaFormCreate, ChamadaFormUpdate, ProjetoModeloForm, TemaFormCreate, TemaFormUpdate, ProjetoModeloUpdateForm, TurmaFormCreate, TurmaFormUpdate
from chamadas.models import Chamada, ProjetoModelo
from pages.forms import NoticiaFormCreate, NoticiaFormUpdate
from .models import CadastroChamada, CadastroProfile, CadastroNoticia, CadastroProjeto, CadastroTema, CadastroTurma
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

    object_list = ProjetoModelo.objects.all()

    if object_list:
        pass
    else:
        ProjetoModelo.objects.create(nome = 'Padrão')
        projeto = ProjetoModelo.objects.get(nome = 'Padrão')
        CadastroProjeto.objects.create(projeto = projeto)

    if request.method == 'POST':
        form = ChamadaFormCreate(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            CadastroChamada.objects.create(chamada = form.instance)
            return HttpResponseRedirect(reverse_lazy('cadastros:chamadas_list'))
    else:
        form = ChamadaFormCreate()

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

@login_required
@user_passes_test(lambda u:u.is_superuser, login_url='users:login')
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

@login_required
@user_passes_test(lambda u:u.is_superuser, login_url='users:login')
def noticia_delete_view(request, pk):

    template_name = 'cadastros/forms_delete.html'

    object = get_object_or_404(CadastroNoticia, pk = pk)

    if request.method == 'POST':
        object.noticia.delete()
        return HttpResponseRedirect(reverse_lazy('cadastros:noticias_list'))

    context = {'object': object}

    return render(request, template_name, context)

# Temas

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def tema_create_view(request):

    template_name = 'cadastros/forms.html'

    if request.method == 'POST':
        form = TemaFormCreate(request.POST)
        if form.is_valid():
            form.save() # criando objeto Tema
            CadastroTema.objects.create(tema = form.instance) # criando objeto CadastroTema
            return HttpResponseRedirect(reverse_lazy('cadastros:temas_list'))
    else:
        form = TemaFormCreate()

    context = {'titulo': 'Novo cadastro de tema', 'botao': 'Salvar', 'form': form}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def tema_list_view(request):

    template_name = 'cadastros/temas_list.html'

    object_list = CadastroTema.objects.all()

    context = {'object_list': object_list}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def tema_update_view(request, pk):

    template_name = 'cadastros/forms.html'

    object = get_object_or_404(CadastroTema, pk = pk)

    if request.method == 'POST':
        form = TemaFormUpdate(request.POST, instance = object.tema)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('cadastros:temas_list'))
    else:
        form = TemaFormUpdate(instance=object.tema)

    context = {'titulo': 'Edição de cadastro de tema', 'botao': 'Salvar', 'form': form}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def tema_delete_view(request, pk):

    template_name = 'cadastros/forms_delete.html'

    object = get_object_or_404(CadastroTema, pk = pk)

    if request.method == 'POST':
        object.tema.delete()
        return HttpResponseRedirect(reverse_lazy('cadastros:temas_list'))

    context = {'object': object}

    return render(request, template_name, context)

# Projeto modelo

@login_required
@user_passes_test(lambda u:u.is_superuser, login_url='users:login')
def projetomodelo_list_view(request):

    template_name = 'cadastros/projetomodelo_list.html'

    object_list = CadastroProjeto.objects.all()

    context = {'object_list': object_list}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u:u.is_superuser, login_url='users:login')
def projetomodelo_create_view(request):

    template_name = 'cadastros/forms.html'

    if request.method == 'POST':
        form = ProjetoModeloForm(request.POST)
        if form.is_valid():
            form.save()
            CadastroProjeto.objects.create(projeto = form.instance)
            return HttpResponseRedirect(reverse_lazy('cadastros:projetomodelo_list'))
    else:
        form = ProjetoModeloForm()

    context = {'titulo': 'Novo cadastro de modelo de projeto', 'botao': 'Salvar', 'form': form}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u:u.is_superuser, login_url='users:login')
def projetomodelo_update_view(request, pk):

    template_name = 'cadastros/forms.html'

    object = get_object_or_404(CadastroProjeto, pk = pk)

    if request.method == 'POST':
        form = ProjetoModeloUpdateForm(request.POST, instance = object.projeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('cadastros:projetomodelo_list'))
    else:
        form = ProjetoModeloUpdateForm(instance = object.projeto)

    context = {'titulo': 'Edição de cadastro de modelo de projeto', 'botao': 'Salvar', 'form': form}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def projetomodelo_delete_view(request, pk):

    template_name = 'cadastros/forms_delete.html'

    cadastroprojeto = get_object_or_404(CadastroProjeto, pk = pk)
    chamada = Chamada.objects.filter(projetomodelo = cadastroprojeto.projeto)

    if chamada.exists():
        depend = Chamada.objects.get(projetomodelo = cadastroprojeto.projeto)
    else:
        depend = None

    if request.method == 'POST':
        cadastroprojeto.projeto.delete()
        return HttpResponseRedirect(reverse_lazy('cadastros:projetomodelo_list'))

    context = {'object': cadastroprojeto, 'depend': depend}

    return render(request, template_name, context)

# turmas

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def turmas_create_view(request):

    template_name = 'cadastros/forms.html'

    if request.method == 'POST':
        form = TurmaFormCreate(request.POST)
        if form.is_valid():
            form.save() # criando objeto Tema
            CadastroTurma.objects.create(turma = form.instance) # criando objeto CadastroTema
            return HttpResponseRedirect(reverse_lazy('cadastros:turmas_list'))
    else:
        form = TurmaFormCreate()

    context = {'titulo': 'Novo cadastro de turma', 'botao': 'Salvar', 'form': form}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def turmas_list_view(request):

    template_name = 'cadastros/turmas_list.html'

    object_list = CadastroTurma.objects.all()

    context = {'object_list': object_list}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def turmas_update_view(request, pk):

    template_name = 'cadastros/forms.html'

    object = get_object_or_404(CadastroTurma, pk = pk)

    if request.method == 'POST':
        form = TurmaFormUpdate(request.POST, instance = object.turma)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('cadastros:turmas_list'))
    else:
        form = TurmaFormUpdate(instance=object.turma)

    context = {'titulo': 'Edição de cadastro de turma', 'botao': 'Salvar', 'form': form}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def turmas_delete_view(request, pk):

    template_name = 'cadastros/forms_delete.html'

    object = get_object_or_404(CadastroTurma, pk = pk)

    if request.method == 'POST':
        object.turma.delete()
        return HttpResponseRedirect(reverse_lazy('cadastros:turmas_list'))

    context = {'object': object}

    return render(request, template_name, context)
