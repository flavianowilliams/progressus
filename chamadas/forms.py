from django import forms
from .models import Chamada

class ChamadaForm(forms.ModelForm):
    class Meta:
        model = Chamada
        fields = [
            'nome',
             'resumo',
              'aviso',
               'deadline_inscricao',
                'deadline_bibliografia',
                'deadline_proposta',
                'deadline_projeto',
                'deadline_chamada',
                'edital',
                ]

    def clean_nome(self):
        data = self.cleaned_data['nome']
        if Chamada.objects.filter(nome = data).exists():
            raise forms.ValidationError('O nome {} já está em uso.'.format(data))
        return data