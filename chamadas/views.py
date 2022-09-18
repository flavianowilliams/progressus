from django.shortcuts import render, get_object_or_404
from chamadas.models import Chamada, Inscricao
from chamadas.forms import InscricaoForm
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
