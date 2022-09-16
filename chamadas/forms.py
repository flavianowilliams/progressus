from django import forms
from .models import Chamada, Tema

class ChamadaFormCreate(forms.ModelForm):

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

class ChamadaFormUpdate(forms.ModelForm):
    
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

class TemaFormCreate(forms.ModelForm):

    class Meta:
        model = Tema
        fields = [
            'titulo',
             'requisitos',
              'descricao',
                ]

    def clean_titulo(self):
        data = self.cleaned_data['titulo']
        if Tema.objects.filter(titulo = data).exists():
            raise forms.ValidationError('O título {} já está em uso.'.format(data))
        return data

class TemaFormUpdate(forms.ModelForm):

    class Meta:
        model = Tema
        fields = [
            'titulo',
             'requisitos',
              'descricao',
                ]
