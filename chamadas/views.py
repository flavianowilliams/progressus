from django.shortcuts import render, get_object_or_404, redirect
from chamadas.models import Chamada, Inscricao, Introducao, Projeto
from chamadas.forms import InscricaoForm, ProjetoForm, ProjetoIntroducaoAdmin, ProjetoAdminForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from progressus.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

# Chamada

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

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def chamada_list_superuser_view(request):

    template_name = 'chamadas/chamadas_list_superuser.html'

    object_list = Chamada.objects.all()

    context = {'object_list': object_list}

    return render(request, template_name, context)

# Inscricao

@login_required
def inscricao_create_view(request, pk):

    template_name = 'chamadas/inscricao_form.html'

    chamada = get_object_or_404(Chamada, pk = pk)

    if Inscricao.objects.filter(lider = request.user.profile, chamada = chamada).exists():
        context = {'chamada': chamada}
        return render(request, 'chamadas/inscricao_erro.html', context)
    else:
        if request.method == 'POST':
            form = InscricaoForm(request.POST)
            if form.is_valid():
                form.instance.chamada = chamada
                form.instance.lider = request.user.profile
                form.save()
                Projeto.objects.create(inscricao = form.instance, modelo = chamada.projetomodelo)
                projeto = Projeto.objects.get(inscricao = form.instance)
                Introducao.objects.create(projeto = projeto)
                sender = EMAIL_HOST_USER
                receiver = form.instance.lider.usuario.email
                message = (
                        'Inscrição feita com sucesso na chamada {} em {}.\n\n'.format(form.instance.chamada, form.instance.created)+
                        'Equipe: {}\n'.format(form.instance.equipe)+
                        'Lider: {}\n'.format(form.instance.lider)+
                        'Membro: {}\n'.format(form.instance.membro_1)+
                        'Membro: {}\n'.format(form.instance.membro_2)+
                        'Membro: {}\n'.format(form.instance.membro_3)
                        )
                subject = 'Plaforma progressus - Inscrição'
                send_mail(subject, message, sender, [receiver], fail_silently=False)
                return HttpResponseRedirect(reverse_lazy('chamadas:chamadas_abertas'))
        else:
            form = InscricaoForm()
            form.instance.lider = request.user.profile

        context = {'botao': 'Inscrever', 'chamada': chamada ,'form': form}
        return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def inscricao_list_superuser(request, pk):

    template_name = 'chamadas/inscricoes_list_superuser.html'

    chamada = get_object_or_404(Chamada, pk = pk)

    object_list = Inscricao.objects.filter(chamada = chamada)

    context = {'object_list': object_list, 'chamada': chamada}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def inscricao_delete_superuser(request, pk):

    template_name = 'cadastros/forms_delete.html'

    object = get_object_or_404(Inscricao, pk = pk)

    if request.method == 'POST':
        object.delete()
        return HttpResponseRedirect(reverse_lazy('chamadas:inscricoes_list_superuser', kwargs = {'pk': object.chamada.pk}))

    context = {'object': object}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def inscricao_update_view(request, pk):

    template_name = 'chamadas/inscricao_editar.html'

    object = get_object_or_404(Inscricao, pk = pk)

    if request.method == 'POST':
        object.delete()
        form = InscricaoForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('chamadas:inscricoes_list_superuser', kwargs = {'pk': object.chamada.pk}))
    else:
        form = InscricaoForm(instance = object)

    context = {'botao': 'Editar', 'form': form}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def enviar_email(request, pk):

    template_name = 'users/email.html'

    inscricao = get_object_or_404(Inscricao, pk = pk)

    sender = EMAIL_HOST_USER
    receiver = inscricao.lider.usuario.email
    subject = 'Plaforma progressus - Atenção!'

    if request.method == 'POST':
        message = request.POST.get('message')
        send_mail(subject, message, sender, [receiver], fail_silently=False)
        return HttpResponseRedirect(reverse_lazy('pages:home'))
    else:
        message = ''

    form = {'from': sender, 'to': receiver, 'message': message, 'subject': subject}

    context = {'nome': inscricao, 'botao': 'Enviar', 'form': form}

    return render(request, template_name, context)

@login_required
def inscricao_list_user(request):

    template_name = 'chamadas/inscricao_list_user.html'

    object_list = Inscricao.objects.filter(lider = request.user.profile)

    context = {'object_list': object_list}

    return render(request, template_name, context)

@login_required
def inscricao_detail_view(request, pk):

    template_name = 'chamadas/inscricao_detail.html'

    object = get_object_or_404(Inscricao, pk = pk, lider = request.user.profile)

    context = {'object': object}

    return render(request, template_name, context)

# projetos

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def projeto_list_view(request, pk):

    template_name = 'chamadas/projetos_list.html'

    object = get_object_or_404(Chamada, pk = pk)

    object_list = Inscricao.objects.filter(chamada = object)

    context = {'object_list': object_list, 'chamada': object}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def projeto_detail_list_view(request, pk):

    template_name = 'chamadas/projetos_detail_list.html'

    chamada = get_object_or_404(Chamada, pk = pk)
    projeto = Projeto.objects.all()

    object_list = [object for object in projeto if object.inscricao.chamada == chamada]

    context = {'object_list': object_list, 'chamada': chamada}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def introducao_detail_superuser(request, pk):

    template_name = 'chamadas/introducao_detail.html'

    object = get_object_or_404(Projeto, pk = pk)

    if request.method == 'POST':
        form = ProjetoIntroducaoAdmin(request.POST, instance=object.introducao)
        if form.is_valid():
            form.save()
            introducao = Introducao.objects.get(projeto = object)
            form.instance.nota_introducao = introducao.setNotaIntroducao()
            form.save()
            object.nota = object.setNota()
            object.save()
            return HttpResponseRedirect(reverse_lazy('chamadas:projeto_detail_superuser', kwargs = {'pk': object.inscricao.chamada.pk}))
    else:
        form = ProjetoIntroducaoAdmin(instance=object.introducao)
        introducao = Introducao.objects.get(projeto = object)
        form.instance.nota_introducao = introducao.setNotaIntroducao()
 
    context = {'form': form}

    return render(request, template_name, context)

# usuario

@login_required
def inscricao_projeto_view(request, pk):

    template_name = 'chamadas/inscricao_projeto.html'

    inscricao = get_object_or_404(Inscricao, pk = pk)

    object = Projeto.objects.get(inscricao = inscricao)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('chamadas:inscricao_detail', kwargs = {'pk': object.inscricao.pk}))
    else:
        form = ProjetoForm(instance=object)

    context = {'form': form}

    return render(request, template_name, context)

@login_required
def inscricao_introducao_view(request, pk):

    template_name = 'chamadas/inscricao_introducao.html'

    inscricao = get_object_or_404(Inscricao, pk = pk)

    object = Introducao.objects.get(projeto = inscricao.projeto)

    if request.method == 'POST':
        form = ProjetoIntroducaoAdmin(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('chamadas:inscricao_detail', kwargs = {'pk': object.projeto.inscricao.pk}))
    else:
        form = ProjetoIntroducaoAdmin(instance=object)

    context = {'form': form}

    return render(request, template_name, context)
