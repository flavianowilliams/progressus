from datetime import date
from django.shortcuts import render, get_object_or_404
from chamadas.models import Apresentacao, Bibliografia, Chamada, Financeiro, Inscricao, Introducao, Metodologia, Projeto, Proposta, Resultado, Teoria, Extra
from chamadas.forms import BibliografiaForm, FinanceiroForm, InscricaoForm, InscricaoUpdateForm, ProjetoApresentacaoAdmin, ProjetoBibliografiaAdmin, ProjetoExtraAdmin, ProjetoFinanceiroAdmin, ProjetoForm, ProjetoIntroducaoAdmin, ProjetoPropostaAdmin, ProjetoTituloForm, PropostaForm, InscricaoStatusAdmin
from chamadas.forms import ProjetoTeoriaAdmin, ProjetoResultadoAdmin
from chamadas.forms import ProjetoMetodologiaAdmin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from progressus.settings import EMAIL_HOST_USER, MEDIA_ROOT
from django.core.mail import send_mail
from chamadas.utils import Valor

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

def projetos_destaque_list_view(request, pk):

    template_name = 'chamadas/projetos_destaque_list.html'

    chamada = get_object_or_404(Chamada, pk = pk)

    inscricao = Inscricao.objects.filter(chamada = chamada)

    object_list = [object for object in inscricao if object.inscricao_status == 'destaque']

    context = {'object_list': object_list, 'chamada': chamada}

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
                Bibliografia.objects.create(inscricao = form.instance, modelo = chamada.projetomodelo)
                Apresentacao.objects.create(inscricao = form.instance, modelo = chamada.projetomodelo)
                Proposta.objects.create(inscricao = form.instance, modelo = chamada.projetomodelo)
                Extra.objects.create(inscricao = form.instance)
                Financeiro.objects.create(inscricao = form.instance)
                projeto = Projeto.objects.get(inscricao = form.instance)
                Introducao.objects.create(projeto = projeto)
                Teoria.objects.create(projeto = projeto)
                Metodologia.objects.create(projeto = projeto)
                Resultado.objects.create(projeto = projeto)
                sender = EMAIL_HOST_USER
                receiver = form.instance.lider.usuario.email
                message = (
                        'Inscrição feita com sucesso na chamada {} em {}.\n\n'.format(form.instance.chamada, form.instance.created)+
                        'Equipe: {}\n'.format(form.instance.equipe)+
                        'Turma: {}\n'.format(form.instance.turma)+
                        'Lider: {}\n'.format(form.instance.lider)+
                        'Membro: {}\n'.format(form.instance.membro_1)+
                        'Membro: {}\n'.format(form.instance.membro_2)+
                        'Membro: {}\n'.format(form.instance.membro_3)+
                        '\nPara maiores informações, acesse http://200.17.101.198/'
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
        form = InscricaoUpdateForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('chamadas:inscricoes_list_superuser', kwargs = {'pk': object.chamada.pk}))
    else:
        form = InscricaoUpdateForm(instance = object)

    context = {'botao': 'Editar', 'form': form}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def inscricao_update_status_view(request, pk):

    template_name = 'chamadas/inscricao_status_editar.html'

    object = get_object_or_404(Inscricao, pk = pk)

    if request.method == 'POST':
        form = InscricaoStatusAdmin(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('chamadas:projetos_list', kwargs = {'pk': object.chamada.pk}))
    else:
        form = InscricaoStatusAdmin(instance = object)

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
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def enviar_email_coletivo(request, pk):

    template_name = 'users/email.html'

    chamada = get_object_or_404(Chamada, pk = pk)

    receiver = [u.lider.usuario.email for u in Inscricao.objects.filter(chamada = chamada)]

    sender = EMAIL_HOST_USER
    subject = 'Plaforma progressus - Atenção!'

    if request.method == 'POST':
        message = request.POST.get('message')
        send_mail(subject, message, sender, receiver, fail_silently=False)
        return HttpResponseRedirect(reverse_lazy('pages:home'))
    else:
        message = ''

    form = {'from': sender, 'to': receiver, 'message': message, 'subject': subject}

    context = {'chamada': chamada, 'botao': 'Enviar', 'form': form}

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

    if request.method == 'POST':
        form = ProjetoTituloForm(request.POST, instance=object.projeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('chamadas:inscricao_detail', kwargs = {'pk': pk}))
    else:
        form = ProjetoTituloForm(instance=object.projeto)

    context = {'object': object, 'form': form}

    return render(request, template_name, context)

# administrador

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def projeto_list_view(request, pk):

    template_name = 'chamadas/projetos_list.html'

    object = get_object_or_404(Chamada, pk = pk)

    object_list = Inscricao.objects.filter(chamada = object).order_by('tema')

    if request.method == 'POST':
        for object in object_list:
            data = float(object.bibliografia.nota_bibliografia)
            data += float(object.projeto.nota_projeto)
            data += float(object.proposta.nota_proposta)
            data += float(object.apresentacao.nota_apresentacao)
            data += float(object.extra.nota_extra)
            object.nota = min(100,data)
            object.save()
        return HttpResponseRedirect(reverse_lazy('chamadas:projetos_list', kwargs = {'pk': pk}))

    context = {'object_list': object_list, 'chamada': object}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def projeto_detail_list_view(request, pk):

    template_name = 'chamadas/projetos_detail_list.html'

    chamada = get_object_or_404(Chamada, pk = pk)
    projeto = Projeto.objects.all().order_by('-arquivo')

    object_list = [object for object in projeto if object.inscricao.chamada == chamada]
  
    if request.method == 'POST':
        for object in projeto:
            object.nota_projeto = object.setNotaProjeto()
            object.save()
        return HttpResponseRedirect(reverse_lazy('chamadas:projeto_detail_superuser', kwargs = {'pk': pk}))

    context = {'object_list': object_list, 'chamada': chamada}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def bibliografia_detail_superuser(request, pk):

    template_name = 'chamadas/bibliografia_detail.html'

    object = get_object_or_404(Inscricao, pk = pk)

    if request.method == 'POST':
        form = ProjetoBibliografiaAdmin(request.POST, instance=object.bibliografia)
        if form.is_valid():
            form.save()
            bibliografia = Bibliografia.objects.get(inscricao = object)
            form.instance.nota_bibliografia = bibliografia.setNotaBibliografia()
            form.save()
            return HttpResponseRedirect(reverse_lazy('chamadas:projetos_list', kwargs = {'pk': object.chamada.pk}))
    else:
        form = ProjetoBibliografiaAdmin(instance=object.bibliografia)
        bibliografia = Bibliografia.objects.get(inscricao = object)
        form.instance.nota_bibliografia = bibliografia.setNotaBibliografia()
 
    context = {'form': form, 'media_root': MEDIA_ROOT}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def apresentacao_detail_superuser(request, pk):

    template_name = 'chamadas/apresentacao_detail.html'

    object = get_object_or_404(Inscricao, pk = pk)

    if request.method == 'POST':
        form = ProjetoApresentacaoAdmin(request.POST, instance=object.apresentacao)
        if form.is_valid():
            form.save()
            apresentacao = Apresentacao.objects.get(inscricao = object)
            form.instance.nota_apresentacao = apresentacao.setNotaApresentacao()
            form.save()
            return HttpResponseRedirect(reverse_lazy('chamadas:projetos_list', kwargs = {'pk': object.chamada.pk}))
    else:
        form = ProjetoApresentacaoAdmin(instance=object.apresentacao)
        apresentacao = Apresentacao.objects.get(inscricao = object)
        form.instance.nota_apresentacao = apresentacao.setNotaApresentacao()
 
    context = {'form': form}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def financeiro_detail_superuser(request, pk):

    template_name = 'chamadas/financeiro_detail.html'

    object = get_object_or_404(Inscricao, pk = pk)

    if request.method == 'POST':
        form = ProjetoFinanceiroAdmin(request.POST, instance=object.financeiro)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('chamadas:projetos_list', kwargs = {'pk': object.chamada.pk}))
    else:
        form = ProjetoFinanceiroAdmin(instance=object.financeiro)
 
    context = {'form': form}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def proposta_detail_superuser(request, pk):

    template_name = 'chamadas/proposta_detail.html'

    object = get_object_or_404(Inscricao, pk = pk)

    if request.method == 'POST':
        form = ProjetoPropostaAdmin(request.POST, instance=object.proposta)
        if form.is_valid():
            form.instance.nota_proposta = object.proposta.setNotaProposta()
            form.save()
            return HttpResponseRedirect(reverse_lazy('chamadas:projetos_list', kwargs = {'pk': object.chamada.pk}))
    else:
        form = ProjetoPropostaAdmin(instance=object.proposta)
 
    context = {'form': form}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def extra_detail_superuser(request, pk):

    template_name = 'chamadas/extra_detail.html'

    object = get_object_or_404(Inscricao, pk = pk)

    if request.method == 'POST':
        form = ProjetoExtraAdmin(request.POST, instance=object.extra)
        if form.is_valid():
            extra = Extra.objects.get(inscricao = object)
            form.instance.nota_extra = extra.setNotaExtra()
            form.save()
            return HttpResponseRedirect(reverse_lazy('chamadas:projetos_list', kwargs = {'pk': object.chamada.pk}))
    else:
        form = ProjetoExtraAdmin(instance=object.extra)
        extra = Extra.objects.get(inscricao = object)
        form.instance.nota_extra = extra.setNotaExtra()
 
    context = {'form': form}

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
#            object.nota = object.setNota()
#            object.save()
            return HttpResponseRedirect(reverse_lazy('chamadas:projeto_detail_superuser', kwargs = {'pk': object.inscricao.chamada.pk}))
    else:
        form = ProjetoIntroducaoAdmin(instance=object.introducao)
        introducao = Introducao.objects.get(projeto = object)
        form.instance.nota_introducao = introducao.setNotaIntroducao()
 
    context = {'form': form}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def teoria_detail_superuser(request, pk):

    template_name = 'chamadas/teoria_detail.html'

    object = get_object_or_404(Projeto, pk = pk)

    if request.method == 'POST':
        form = ProjetoTeoriaAdmin(request.POST, instance=object.teoria)
        if form.is_valid():
            form.save()
            teoria = Teoria.objects.get(projeto = object)
            form.instance.nota_teoria = teoria.setNotaTeoria()
            form.save()
#            object.nota = object.setNota()
#            object.save()
            return HttpResponseRedirect(reverse_lazy('chamadas:projeto_detail_superuser', kwargs = {'pk': object.inscricao.chamada.pk}))
    else:
        form = ProjetoTeoriaAdmin(instance=object.teoria)
        teoria = Teoria.objects.get(projeto = object)
        form.instance.nota_teoria = teoria.setNotaTeoria()
 
    context = {'form': form}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def metodologia_detail_superuser(request, pk):

    template_name = 'chamadas/metodologia_detail.html'

    object = get_object_or_404(Projeto, pk = pk)

    if request.method == 'POST':
        form = ProjetoMetodologiaAdmin(request.POST, instance=object.metodologia)
        if form.is_valid():
            form.save()
            metodologia = Metodologia.objects.get(projeto = object)
            form.instance.nota_metodologia = metodologia.setNotaMetodologia()
            form.save()
            return HttpResponseRedirect(reverse_lazy('chamadas:projeto_detail_superuser', kwargs = {'pk': object.inscricao.chamada.pk}))
    else:
        form = ProjetoMetodologiaAdmin(instance=object.metodologia)
        metodologia = Metodologia.objects.get(projeto = object)
        form.instance.nota_metodologia = metodologia.setNotaMetodologia()
 
    context = {'form': form}

    return render(request, template_name, context)

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='users:login')
def resultado_detail_superuser(request, pk):

    template_name = 'chamadas/resultado_detail.html'

    object = get_object_or_404(Projeto, pk = pk)
    resultado = Resultado.objects.get(projeto = object)

    if request.method == 'POST':
        form = ProjetoResultadoAdmin(request.POST, instance=resultado)
        if form.is_valid():

            form.save()

            kwargs = {
                'tema': object.inscricao.tema,
                'atributo': 'resultado_fback_1',
                'regra': object.modelo.resultado_prop_1,
                'valor': form.cleaned_data['resultado_fback_1']
                }

            form.instance.resultado_nota_1 = Valor(kwargs).setValor()

#            args = {
#                'tema': object.inscricao.tema,
#                'atributo': 'resultado_fback_2',
#                'regra': object.modelo.resultado_prop_2,
#                'valor': form.cleaned_data['resultado_fback_2']
#                }
#
#            form.instance.resultado_nota_2 = Valor(args).setValor()

            form.instance.nota_resultado = resultado.setNotaResultado()

            form.save()

            return HttpResponseRedirect(reverse_lazy('chamadas:projeto_detail_superuser', kwargs = {'pk': object.inscricao.chamada.pk}))
    else:
        form = ProjetoResultadoAdmin(instance=resultado)
        form.instance.nota_resultado = resultado.setNotaResultado()
 
    context = {'form': form}

    return render(request, template_name, context)

# usuario

@login_required
def inscricao_projeto_view(request, pk):

    template_name = 'chamadas/inscricao_projeto.html'

    inscricao = get_object_or_404(Inscricao, pk = pk, lider=request.user.profile)

    object = get_object_or_404(Projeto, inscricao = inscricao)
    resultado = get_object_or_404(Resultado, projeto = object)

    input_1 = [resultado.resultado_fback_1 for resultado in Resultado.objects.all()]
    input_2 = [resultado.resultado_fback_2 for resultado in Resultado.objects.all()]

    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            resultado.resultado_input_1 = form.cleaned_data['resultado_1']
            resultado.resultado_fback_1 = form.cleaned_data['resultado_1']
            resultado.resultado_input_2 = form.cleaned_data['resultado_2']
            resultado.resultado_fback_2 = form.cleaned_data['resultado_2']
            resultado.save()
            form.save()
            sender = EMAIL_HOST_USER
            receiver = inscricao.lider.usuario.email
            message = (
                        'Você enviou os resultados do seu trabalho em {}.\n\n'.format(date.today())+
                        'Para maiores informações, acesse http://200.17.101.198/'
                        )
            subject = 'Plaforma progressus - Resultados'
            send_mail(subject, message, sender, [receiver], fail_silently=False)
            return HttpResponseRedirect(reverse_lazy('chamadas:inscricao_detail', kwargs = {'pk': object.inscricao.pk}))
    else:
        form = ProjetoForm(instance=object)

    context = {'form': form,
    'max_input_1': max(input_1),
    'max_input_2': max(input_2),
    'min_input_1': min(input_1),
    'min_input_2': min(input_2),
    }

    return render(request, template_name, context)

@login_required
def inscricao_bibliografia_view(request, pk):

    template_name = 'chamadas/inscricao_bibliografia.html'

    inscricao = get_object_or_404(Inscricao, pk = pk, lider=request.user.profile)

    object = get_object_or_404(Bibliografia, inscricao = inscricao)

    if request.method == 'POST':
        form = BibliografiaForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('chamadas:inscricao_detail', kwargs = {'pk': inscricao.pk}))
    else:
        form = BibliografiaForm(instance=object)

    context = {'form': form}

    return render(request, template_name, context)

@login_required
def inscricao_apresentacao_view(request, pk):

    template_name = 'chamadas/inscricao_apresentacao.html'

    inscricao = get_object_or_404(Inscricao, pk = pk, lider=request.user.profile)

    object = get_object_or_404(Apresentacao, inscricao = inscricao)

    if request.method == 'POST':
        form = BibliografiaForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('chamadas:inscricao_detail', kwargs = {'pk': inscricao.pk}))
    else:
        form = BibliografiaForm(instance=object)

    context = {'form': form}

    return render(request, template_name, context)

@login_required
def inscricao_financeiro_view(request, pk):

    template_name = 'chamadas/inscricao_financeiro.html'

    inscricao = get_object_or_404(Inscricao, pk = pk, lider=request.user.profile)

    object = get_object_or_404(Financeiro, inscricao = inscricao)

    if request.method == 'POST':
        form = FinanceiroForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('chamadas:inscricao_detail', kwargs = {'pk': inscricao.pk}))
    else:
        form = FinanceiroForm(instance=object)

    context = {'form': form}

    return render(request, template_name, context)

@login_required
def inscricao_proposta_view(request, pk):

    template_name = 'chamadas/inscricao_proposta.html'

    inscricao = get_object_or_404(Inscricao, pk = pk, lider=request.user.profile)

    object = get_object_or_404(Proposta, inscricao = inscricao)

    if request.method == 'POST':
        form = PropostaForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('chamadas:inscricao_detail', kwargs = {'pk': inscricao.pk}))
    else:
        form = PropostaForm(instance=object)

    context = {'form': form}

    return render(request, template_name, context)

@login_required
def inscricao_extra_view(request, pk):

    template_name = 'chamadas/inscricao_extra.html'

    inscricao = get_object_or_404(Inscricao, pk = pk, lider=request.user.profile)

    object = get_object_or_404(Extra, inscricao = inscricao)

    context = {'object': object}

    return render(request, template_name, context)

@login_required
def inscricao_introducao_view(request, pk):

    template_name = 'chamadas/inscricao_introducao.html'

    inscricao = get_object_or_404(Inscricao, pk = pk, lider=request.user.profile)

    object = get_object_or_404(Introducao, projeto = inscricao.projeto)

    if request.method == 'POST':
        form = ProjetoIntroducaoAdmin(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('chamadas:inscricao_detail', kwargs = {'pk': object.projeto.inscricao.pk}))
    else:
        form = ProjetoIntroducaoAdmin(instance=object)

    context = {'form': form}

    return render(request, template_name, context)

@login_required
def ranking_list(request, pk):

    template_name = 'chamadas/ranking_list.html'

    chamada = get_object_or_404(Chamada, pk = pk)

    object_list = Inscricao.objects.filter(chamada = chamada)

    context = {'object_list': object_list}

    return render(request, template_name, context)
