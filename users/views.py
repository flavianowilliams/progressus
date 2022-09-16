from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from cadastros.models import CadastroProfile
from progressus.settings import EMAIL_HOST_USER
from users.forms import ProfileCreation, UserCreation
from django.contrib.auth.models import Group
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView
from django.views.generic.edit import CreateView
from users.models import Profile
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Create your views here.

class UserCreateView(CreateView):
    template_name = "users/forms.html"
    form_class = UserCreation
    success_url = reverse_lazy("users:login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"
        return context

    def form_valid(self, form):
        if Group.objects.filter(name="users").exists() == False:
            Group.objects.create(name="users")
        grupo = get_object_or_404(Group, name="users")
        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()
        profile = Profile.objects.create(usuario=self.object)
        CadastroProfile.objects.create(profile = profile)
        return url

#def user_create_view(request):
#    template_name = "users/forms.html"
#    form_class = UserCreation
#    form = form_class
#
#    if request.method == 'POST':
#        form = form_class(request.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect(reverse_lazy('pages:home'))
#
#    context = {'titulo': 'Registro de cadastro de usuário', 'botao': 'Cadastrar', 'form': form}
#
#    return render(request, template_name, context)

@login_required
def profile_update_view(request):
    template_name = "users/forms.html"
    form_class = ProfileCreation
#
    object = get_object_or_404(Profile, usuario = request.user)
#
    if request.method == 'POST':
        form = form_class(request.POST, instance = object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('pages:home'))
    else:
        form = form_class(instance = object)
#
    context = {'titulo': 'Registro de cadastro de usuário', 'botao': 'Cadastrar', 'form': form}
#
    return render(request, template_name, context)

# reset de senha

class PasswordReset(PasswordResetView):
    template_name='users/password_reset.html'
    email_template_name='users/password_reset_email.html'
    success_url=reverse_lazy('users:password_reset_done')

class PasswordResetDone(PasswordResetDoneView):
    template_name='users/password_reset_done.html'

class PasswordResetConfirm(PasswordResetConfirmView):
    template_name='users/password_reset_confirm.html'
    success_url=reverse_lazy('users:password_reset_complete')

class PasswordResetComplete(PasswordResetCompleteView):
    template_name='users/password_reset_complete.html'

# email

def enviar_email(request, pk):

    template_name = 'users/email.html'

    usuario = get_object_or_404(Profile, pk = pk)

    sender = EMAIL_HOST_USER
    receiver = usuario.usuario.email
    subject = 'Plaforma progressus - Aviso!'

    if request.method == 'POST':
        message = request.POST.get('message')
        send_mail(subject, message, sender, [receiver], fail_silently=False)
        return HttpResponseRedirect(reverse_lazy('pages:home'))
    else:
        message = ''

    form = {'from': sender, 'to': receiver, 'message': message, 'subject': subject}

    context = {'nome': usuario.nome_completo, 'botao': 'Enviar', 'form': form}

    return render(request, template_name, context)
