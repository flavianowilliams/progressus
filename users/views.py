from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from users.forms import UserCreation
from django.contrib.auth.models import Group
from django.views.generic.edit import CreateView

# Create your views here.

#def user_create_view(request):
#    template_name = "users/forms.html"
#    form_class = UserCreation
#    form = form_class
#
#    grupo = Group.objects.get(name='users')
#
#    if request.method == 'POST':
#        form = form_class(request.POST)
#        if form.is_valid():
#            usuario = form.Meta.model.username
#            usuario.groups.add(grupo)
#            form.save()
#            return HttpResponseRedirect(reverse_lazy('pages:home'))
#
#    context = {'titulo': 'Registro de novo usuário', 'botao': 'Cadastrar', 'form': form}
#
#    return render(request, template_name, context)
#
class UserCreateView(CreateView):
    template_name = "users/forms.html"
    form_class = UserCreation
    success_url = reverse_lazy("pages:home")

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
#        Profile.objects.create(usuario=self.object)
        return url
