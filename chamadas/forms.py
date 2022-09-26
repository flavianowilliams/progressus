from email.policy import default
from django import forms
from .models import Apresentacao, Bibliografia, Chamada, Extra, Financeiro, Introducao, Metodologia, ProjetoModelo, Proposta, Tema, Inscricao, Projeto, Teoria, Resultado

class ChamadaFormCreate(forms.ModelForm):

    class Meta:
        model = Chamada
        fields = [
            'nome',
             'resumo',
              'aviso',
              'orcamento',
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
              'orcamento',
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
            'metodologia_titulo_1',
             'metodologia_peso_1',
            'metodologia_titulo_2',
             'metodologia_peso_2',
            'metodologia_titulo_3',
             'metodologia_peso_3',
            'metodologia_titulo_4',
             'metodologia_peso_4',
            'metodologia_titulo_5',
             'metodologia_peso_5',
            'apresentacao_titulo_1',
             'apresentacao_peso_1',
            'apresentacao_titulo_2',
             'apresentacao_peso_2',
            'apresentacao_titulo_3',
             'apresentacao_peso_3',
            'apresentacao_titulo_4',
             'apresentacao_peso_4',
            'apresentacao_titulo_5',
             'apresentacao_peso_5',
             'resultado_peso_1',
             'resultado_peso_2',
             'resultado_peso_3',
             'resultado_peso_4',
             'resultado_peso_5',
             'introducao_peso',
             'teoria_peso',
             'metodologia_peso',
             'resultado_peso',
             'apresentacao_peso',
             'bibliografia_peso',
             'proposta_peso',
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
            'metodologia_titulo_1',
             'metodologia_peso_1',
            'metodologia_titulo_2',
             'metodologia_peso_2',
            'metodologia_titulo_3',
             'metodologia_peso_3',
            'metodologia_titulo_4',
             'metodologia_peso_4',
            'metodologia_titulo_5',
             'metodologia_peso_5',
            'apresentacao_titulo_1',
             'apresentacao_peso_1',
            'apresentacao_titulo_2',
             'apresentacao_peso_2',
            'apresentacao_titulo_3',
             'apresentacao_peso_3',
            'apresentacao_titulo_4',
             'apresentacao_peso_4',
            'apresentacao_titulo_5',
             'apresentacao_peso_5',
             'resultado_peso_1',
             'resultado_peso_2',
             'resultado_peso_3',
             'resultado_peso_4',
             'resultado_peso_5',
             'introducao_peso',
             'teoria_peso',
             'metodologia_peso',
             'resultado_peso',
             'apresentacao_peso',
             'bibliografia_peso',
             'proposta_peso',
                ]

class ProjetoForm(forms.ModelForm):

    resultado_input_1 = forms.DecimalField()
    resultado_input_2 = forms.DecimalField()

    class Meta:
        model = Projeto
        fields = [
            'titulo',
            'arquivo',
                ]

class BibliografiaForm(forms.ModelForm):

    class Meta:
        model = Bibliografia
        fields = [
            'arquivo',
                ]

class FinanceiroForm(forms.ModelForm):

    class Meta:
        model = Financeiro
        fields = [
            'comprovante_1',
            'comprovante_2',
            'comprovante_3',
                ]

class PropostaForm(forms.ModelForm):

    class Meta:
        model = Proposta
        fields = [
            'conteudo',
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
            'introducao_consideracao_1',
            'introducao_consideracao_2',
            'introducao_consideracao_3',
            'introducao_consideracao_4',
            'introducao_consideracao_5',
            'nota_introducao',
        ]

class ProjetoApresentacaoAdmin(forms.ModelForm):

    class Meta:
        model = Apresentacao
        fields = [
            'apresentacao_nota_1',
            'apresentacao_nota_2',
            'apresentacao_nota_3',
            'apresentacao_nota_4',
            'apresentacao_nota_5',
            'apresentacao_consideracao_1',
            'apresentacao_consideracao_2',
            'apresentacao_consideracao_3',
            'apresentacao_consideracao_4',
            'apresentacao_consideracao_5',
            'nota_apresentacao',
        ]

class ProjetoPropostaAdmin(forms.ModelForm):

    class Meta:
        model = Proposta
        fields = [
            'consideracoes',
            'proposta_status',
            'nota_proposta',
        ]

class ProjetoFinanceiroAdmin(forms.ModelForm):

    class Meta:
        model = Financeiro
        fields = [
            'consideracoes',
        ]

class ProjetoExtraAdmin(forms.ModelForm):

    class Meta:
        model = Extra
        fields = [
            'penalidade_consideracao',
            'penalidade_nota',
            'divulgacao_consideracao',
            'divulgacao_nota',
        ]

class ProjetoTeoriaAdmin(forms.ModelForm):

    class Meta:
        model = Teoria
        fields = [
            'teoria_total',
            'teoria_qde',
            'teoria_consideracao',
            'nota_teoria',
        ]

class ProjetoMetodologiaAdmin(forms.ModelForm):

    class Meta:
        model = Metodologia
        fields = [
            'metodologia_nota_1',
            'metodologia_nota_2',
            'metodologia_nota_3',
            'metodologia_nota_4',
            'metodologia_nota_5',
            'metodologia_consideracao_1',
            'metodologia_consideracao_2',
            'metodologia_consideracao_3',
            'metodologia_consideracao_4',
            'metodologia_consideracao_5',
            'nota_metodologia',
        ]

class ProjetoResultadoAdmin(forms.ModelForm):

    class Meta:
        model = Resultado
        fields = [
            'resultado_input_1',
            'resultado_input_2',
            'resultado_fback_1',
            'resultado_fback_2',
            'resultado_nota_1',
            'resultado_nota_2',
            'nota_resultado',
        ]

class ProjetoBibliografiaAdmin(forms.ModelForm):

    class Meta:
        model = Bibliografia
        fields = [
            'bibliografia_qde',
            'consideracoes',
            'nota_bibliografia',
        ]

class ProjetoAdminForm(forms.ModelForm):

    class Meta:
        model = Projeto
        fields = [
            'nota_projeto',
                ]
