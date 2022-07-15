from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from users.forms import ProfileCreation, UserCreation
from django.contrib.auth.models import Group
from django.views.generic.edit import CreateView
from users.models import Profile
from django.contrib.auth.decorators import login_required

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
        Profile.objects.create(usuario=self.object)
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
