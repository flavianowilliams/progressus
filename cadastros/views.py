from django.shortcuts import render
from .models import CadastroProfile
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

@login_required
@user_passes_test(lambda u:u.is_superuser, login_url='users:login')
def perfis_list_view(request):
    template_name = 'cadastros/profiles_list.html'
    object_list = CadastroProfile.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)