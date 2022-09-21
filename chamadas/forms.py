from dataclasses import fields
from django import forms
from .models import Chamada, Introducao, ProjetoModelo, Tema, Inscricao, Projeto

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
                'projetomodelo',
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
                'projetomodelo',
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

class InscricaoForm(forms.ModelForm):

    class Meta:
        model = Inscricao
        fields = [
            'equipe',
            'tema',
            'membro_1',
             'membro_2',
              'membro_3',
                ]

    def clean_equipe(self):
        data = self.cleaned_data['equipe']
        if Inscricao.objects.filter(equipe = data).exists():
            raise forms.ValidationError('O nome {} já está em uso.'.format(data))
        return data

    def clean_membro_1(self):
        data = self.cleaned_data['membro_1']
        if Inscricao.objects.filter(membro_1 = data).exists():
            raise forms.ValidationError('O nome {} já está em uso.'.format(data))
        return data

    def clean_membro_2(self):
        data = self.cleaned_data['membro_2']
        if Inscricao.objects.filter(membro_2 = data).exists():
            raise forms.ValidationError('{} já pertence a alguma equipe.'.format(data))
        return data

    def clean_membro_3(self):
        data = self.cleaned_data['membro_3']
        if Inscricao.objects.filter(membro_3 = data).exists():
            raise forms.ValidationError('{} já pertence a alguma equipe.'.format(data))
        return data

class ProjetoModeloForm(forms.ModelForm):

    class Meta:
        model = ProjetoModelo
        fields = [
            'nome',
            'bibliografia_total',
            'introducao_titulo_1',
             'introducao_peso_1',
            'introducao_titulo_2',
             'introducao_peso_2',
            'introducao_titulo_3',
             'introducao_peso_3',
            'introducao_titulo_4',
             'introducao_peso_4',
            'introducao_titulo_5',
             'introducao_peso_5',
             'introducao_peso',
                ]

    def clean_nome(self):
        data = self.cleaned_data['nome']
        if ProjetoModelo.objects.filter(nome = data).exists():
            raise forms.ValidationError('O nome {} já está em uso.'.format(data))
        return data

class ProjetoModeloUpdateForm(forms.ModelForm):

    class Meta:
        model = ProjetoModelo
        fields = [
            'nome',
            'bibliografia_total',
            'introducao_titulo_1',
             'introducao_peso_1',
            'introducao_titulo_2',
             'introducao_peso_2',
            'introducao_titulo_3',
             'introducao_peso_3',
            'introducao_titulo_4',
             'introducao_peso_4',
            'introducao_titulo_5',
             'introducao_peso_5',
             'introducao_peso',
                ]

class ProjetoForm(forms.ModelForm):

    class Meta:
        model = Projeto
        fields = [
            'modelo',
                ]

class ProjetoIntroducaoAdmin(forms.ModelForm):

    class Meta:
        model = Introducao
        fields = [
            'introducao_nota_1',
            'introducao_nota_2',
            'introducao_nota_3',
            'introducao_nota_4',
            'introducao_nota_5',
            'nota_introducao',
        ]

class ProjetoAdminForm(forms.ModelForm):

    class Meta:
        model = Projeto
        fields = [
            'nota',
                ]
