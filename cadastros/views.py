from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from .models import CadastroProfile
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