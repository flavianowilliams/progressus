from datetime import date
from email.policy import default
from django.db import models
from users.models import Profile

# Create your models here.

class ProjetoModelo(models.Model):
    nome = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    bibliografia_total = models.IntegerField(default=10, blank=True)

    introducao_titulo_1 = models.CharField(
        max_length=100,
        default='Qual é o significado?',
        verbose_name = '1. Introdução (parâmetro): Título'
        )
    introducao_peso_1 = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.002,
        verbose_name='2. Introdução (parâmetro): Peso'
        )
    introducao_titulo_2 = models.CharField(
        max_length=100,
        default='Qual é a utilidade?',
        verbose_name = '2. Introdução (parâmetro): Título'
        )
    introducao_peso_2 = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.002,
        verbose_name='2. Introdução (parâmetro): Peso'
        )
    introducao_titulo_3 = models.CharField(
        max_length=100,
        default='Quais as vantagens e desvantagens?',
        verbose_name = '3. Introdução (parâmetro): Título'
        )
    introducao_peso_3 = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.002,
        verbose_name='3. Introdução (parâmetro): Peso'
        )
    introducao_titulo_4 = models.CharField(
        max_length=100,
        default='O que já foi feito sobre o assunto?',
        verbose_name = '4. Introdução (parâmetro): Título'
        )
    introducao_peso_4 = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.002,
        verbose_name='4. Introdução (parâmetro): Peso'
        )
    introducao_titulo_5 = models.CharField(
        max_length=100,
        default='As referências bibliográficas foram citadas corretamente?',
        verbose_name = '5. Introdução (parâmetro): Título'
        )
    introducao_peso_5 = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.002,
        verbose_name='5. Introdução (parâmetro): Peso'
        )

    metodologia_titulo_1 = models.CharField(
        max_length=100,
        default='Como o equipamento ou experimento poderia ser reproduzido?',
        verbose_name = '1. Metodologia (parâmetro): Título'
        )
    metodologia_peso_1 = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.002,
        verbose_name='2. Metodologia (parâmetro): Peso'
        )
    metodologia_titulo_2 = models.CharField(
        max_length=100,
        default='A lista de materiais e/ou softwares necessários foi fornecido?',
        verbose_name = '2. Metodologia (parâmetro): Título'
        )
    metodologia_peso_2 = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.002,
        verbose_name='2. Metodologia (parâmetro): Peso'
        )
    metodologia_titulo_3 = models.CharField(
        max_length=100,
        default='O custo financeiro total ou detalhado por item foi fornecido?',
        verbose_name = '3. Metodologia (parâmetro): Título'
        )
    metodologia_peso_3 = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.002,
        verbose_name='3. Metodologia (parâmetro): Peso'
        )
    metodologia_titulo_4 = models.CharField(
        max_length=100,
        default='O procedimento para a perfeita utilização foi apresentado de maneira clara e objetiva?',
        verbose_name = '4. Metodologia (parâmetro): Título'
        )
    metodologia_peso_4 = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.002,
        verbose_name='4. Metodologia (parâmetro): Peso'
        )
    metodologia_titulo_5 = models.CharField(
        max_length=100,
        default='Uma imagem clara do dispositivo, ou no caso de software o link para o seu repositório foi fornecido?',
        verbose_name = '5. Metodologia (parâmetro): Título'
        )
    metodologia_peso_5 = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.002,
        verbose_name='5. Metodologia (parâmetro): Peso'
        )

    resultado_peso_1 = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.005,
        verbose_name='1. Resultado (parâmetro): Peso'
        )

    resultado_peso_2 = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.005,
        verbose_name='2. Resultado (parâmetro): Peso'
        )

    resultado_peso_3 = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.0,
        verbose_name='3. Resultado (parâmetro): Peso'
        )

    resultado_peso_4 = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.0,
        verbose_name='4. Resultado (parâmetro): Peso'
        )

    resultado_peso_5 = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.0,
        verbose_name='5. Resultado (parâmetro): Peso'
        )

    introducao_peso = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=10,
        verbose_name='Introdução: Peso'
        )

    teoria_peso = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=25,
        verbose_name='Teoria: Peso'
        )

    metodologia_peso = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=10,
        verbose_name='Metodologia: Peso'
        )

    resultado_peso = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=25,
        verbose_name='Resultado: Peso'
        )

    apresentacao_peso = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=10,
        verbose_name='Apresentação: Peso'
        )

    bibliografia_peso = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=10,
        verbose_name='Bibliografia: Peso'
        )

    proposta_peso = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=10,
        verbose_name='Proposta: Peso'
        )

    apresentacao_titulo_1 = models.CharField(
        max_length=100,
        default='A apresentação aconteceu no tempo previsto?',
        verbose_name = '1. Apresentação (parâmetro): Título'
        )
    apresentacao_peso_1 = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.002,
        verbose_name='2. Apresentação (parâmetro): Peso'
        )
    apresentacao_titulo_2 = models.CharField(
        max_length=100,
        default='O apresentador mostrou ter domínio dos conceitos teóricos?',
        verbose_name = '2. Apresentação (parâmetro): Título'
        )
    apresentacao_peso_2 = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.002,
        verbose_name='2. Apresentação (parâmetro): Peso'
        )
    apresentacao_titulo_3 = models.CharField(
        max_length=100,
        default='Qualidade dos recursos audiovisuais (aspectos visuais e auditivos, qualidade das imagens, vídeos e texto)',
        verbose_name = '3. Apresentação (parâmetro): Título'
        )
    apresentacao_peso_3 = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.002,
        verbose_name='3. Apresentação (parâmetro): Peso'
        )
    apresentacao_titulo_4 = models.CharField(
        max_length=100,
        default='A apresentação ocorreu de maneira clara e objetiva?',
        verbose_name = '4. Apresentação (parâmetro): Título'
        )
    apresentacao_peso_4 = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.002,
        verbose_name='4. Apresentação (parâmetro): Peso'
        )
    apresentacao_titulo_5 = models.CharField(
        max_length=100,
        default='Organização dos slides e da apresentação',
        verbose_name = '5. Apresentação (parâmetro): Título'
        )
    apresentacao_peso_5 = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.002,
        verbose_name='5. Apresentação (parâmetro): Peso'
        )

    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=9, null=True, default="STDE")
    total_alunos = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Chamada(models.Model):
    nome = models.CharField(max_length=7, unique=True)
    projetomodelo = models.ForeignKey(ProjetoModelo, on_delete=models.PROTECT, null=True)
    deadline_inscricao = models.DateField(verbose_name='Data limite da inscrição', null=True)
    deadline_bibliografia = models.DateField(verbose_name='Data limite da bibliografia', null=True)
    deadline_proposta = models.DateField(verbose_name='Data limite da proposta', null=True)
    deadline_projeto = models.DateField(verbose_name='Data limite do projeto', null=True)
    deadline_chamada = models.DateField(verbose_name='Data limite da chamada', null=True)
    orcamento = models.DecimalField(max_digits=6, decimal_places=3, default=0.0, blank=True)
    resumo = models.TextField()
    edital = models.FileField(upload_to='pdf/%Y/%m/%d/')
    aviso = models.TextField(null=True, blank=True)

    def get_status(self):
        if date.today() > self.deadline_inscricao:
            if date.today() > self.deadline_chamada:
                data = "Encerrado"
            else:
                data = "Em andamento"
        else:
            data = "Aberto"
        return data

    def get_bibliografia(self):
        if date.today() > self.deadline_bibliografia:
            return False
        else:
            return True

    def get_proposta(self):
        if date.today() > self.deadline_proposta:
            return False
        else:
            return True

    def get_projeto(self):
        if date.today() > self.deadline_projeto:
            return False
        else:
            return True

    def __str__(self):
        return self.nome

class Tema(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    requisitos = models.TextField()

    def __str__(self):
        return self.titulo

class Inscricao(models.Model):
    created = models.DateField(auto_now_add=True)
    tema = models.ForeignKey(Tema, on_delete=models.PROTECT)
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT)
    lider = models.ForeignKey(Profile, on_delete=models.CASCADE)
    chamada = models.ForeignKey(Chamada, on_delete=models.CASCADE)
    equipe = models.CharField(max_length=100)
    membro_1 = models.CharField(max_length=100, null=True, blank=True)
    membro_2 = models.CharField(max_length=100, null=True, blank=True)
    membro_3 = models.CharField(max_length=100, null=True, blank=True)
    nota = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    ranking = models.IntegerField(null=True)

    def __str__(self):
        return self.equipe

class Projeto(models.Model):

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    inscricao = models.OneToOneField(Inscricao, on_delete=models.CASCADE)
    modelo = models.ForeignKey(ProjetoModelo, on_delete=models.PROTECT)

    titulo = models.CharField(max_length=100, null=True, blank=True)

    nota_projeto = models.DecimalField(
        max_digits=6,
        default=0.0,
        decimal_places=3,
        blank=True
        )

    arquivo = models.FileField(upload_to='pdf/%Y/%m/%d/', null=True)
    resumo = models.TextField(null=True, blank=True)
    imagem = models.ImageField(upload_to='img/', max_length=100, null=True, blank=True)

    def setNotaProjeto(self):
        data = float(self.introducao.nota_introducao)
        data += float(self.teoria.nota_teoria)
        data += float(self.metodologia.nota_metodologia)
        data += float(self.resultado.nota_resultado)
        return data

    def __str__(self):
        return self.titulo

class Introducao(models.Model):

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    projeto = models.OneToOneField(Projeto, on_delete=models.CASCADE)

    introducao_nota_1 = models.DecimalField(max_digits=7, decimal_places=3, default=0.0, blank=True)
    introducao_nota_2 = models.DecimalField(max_digits=7, decimal_places=3, default=0.0, blank=True)
    introducao_nota_3 = models.DecimalField(max_digits=7, decimal_places=3, default=0.0, blank=True)
    introducao_nota_4 = models.DecimalField(max_digits=7, decimal_places=3, default=0.0, blank=True)
    introducao_nota_5 = models.DecimalField(max_digits=7, decimal_places=3, default=0.0, blank=True)

    introducao_consideracao_1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default='A equipe não enviou o relatório do trabalho'
        )
    
    introducao_consideracao_2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default='A equipe não enviou o relatório do trabalho'
        )
    introducao_consideracao_3 = models.CharField(
        max_length=255,
        null=True,
        blank=True
        default='A equipe não enviou o relatório do trabalho'
        )
    introducao_consideracao_4 = models.CharField(
        max_length=255,
        null=True,
        blank=True
        default='A equipe não enviou o relatório do trabalho'
        )
    introducao_consideracao_5 = models.CharField(
        max_length=255,
        null=True,
        blank=True
        default='A equipe não enviou o relatório do trabalho'
        )

    nota_introducao = models.DecimalField(
        max_digits=7,
        default=0.0,
        decimal_places=3,
        blank=True
        )

    def setNotaIntroducao(self):
        data = float(self.projeto.modelo.introducao_peso_1)*float(self.introducao_nota_1)
        data += float(self.projeto.modelo.introducao_peso_2)*float(self.introducao_nota_2)
        data += float(self.projeto.modelo.introducao_peso_3)*float(self.introducao_nota_3)
        data += float(self.projeto.modelo.introducao_peso_4)*float(self.introducao_nota_4)
        data += float(self.projeto.modelo.introducao_peso_5)*float(self.introducao_nota_5)
        data = data*float(self.projeto.modelo.introducao_peso)
        return data

class Teoria(models.Model):

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    teoria_total = models.IntegerField(default=0, blank=True)
    teoria_qde = models.IntegerField(default=0, blank=True)
    teoria_consideracao = models.CharField(max_length=255, null=True, blank=True)

    nota_teoria = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.0,
        blank=True
        )

    projeto = models.OneToOneField(Projeto, on_delete=models.CASCADE)

    def setNotaTeoria(self):
        data = 0.0
        try:
            data = float(self.teoria_qde)/float(self.teoria_total)
            data = data*float(self.projeto.modelo.teoria_peso)
        except:
            self.teoria_total = 0
        return data

class Metodologia(models.Model):

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    metodologia_nota_1 = models.DecimalField(max_digits=7, decimal_places=3, default=0.0, blank=True)
    metodologia_nota_2 = models.DecimalField(max_digits=7, decimal_places=3, default=0.0, blank=True)
    metodologia_nota_3 = models.DecimalField(max_digits=7, decimal_places=3, default=0.0, blank=True)
    metodologia_nota_4 = models.DecimalField(max_digits=7, decimal_places=3, default=0.0, blank=True)
    metodologia_nota_5 = models.DecimalField(max_digits=7, decimal_places=3, default=0.0, blank=True)
    metodologia_consideracao_1 = models.CharField(max_length=255, null=True, blank=True)
    metodologia_consideracao_2 = models.CharField(max_length=255, null=True, blank=True)
    metodologia_consideracao_3 = models.CharField(max_length=255, null=True, blank=True)
    metodologia_consideracao_4 = models.CharField(max_length=255, null=True, blank=True)
    metodologia_consideracao_5 = models.CharField(max_length=255, null=True, blank=True)

    nota_metodologia = models.DecimalField(max_digits=7, decimal_places=3, default=0.0, blank=True)

    projeto = models.OneToOneField(Projeto, on_delete=models.CASCADE)

    def setNotaMetodologia(self):
        data = float(self.projeto.modelo.metodologia_peso_1)*float(self.metodologia_nota_1)
        data += float(self.projeto.modelo.metodologia_peso_2)*float(self.metodologia_nota_2)
        data += float(self.projeto.modelo.metodologia_peso_3)*float(self.metodologia_nota_3)
        data += float(self.projeto.modelo.metodologia_peso_4)*float(self.metodologia_nota_4)
        data += float(self.projeto.modelo.metodologia_peso_5)*float(self.metodologia_nota_5)
        data = data*float(self.projeto.modelo.metodologia_peso)
        return data

class Resultado(models.Model):

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    resultado_input_1 = models.DecimalField(
        max_digits=7,
        decimal_places=3,
        default=0.0, blank=True)

    resultado_input_2 = models.DecimalField(
        max_digits=7,
        decimal_places=3,
        default=0.0,
        blank=True)

    resultado_input_3 = models.DecimalField(
        max_digits=7,
        decimal_places=3,
        default=0.0,
        blank=True)

    resultado_input_4 = models.DecimalField(
        max_digits=7,
        decimal_places=3,
        default=0.0,
        blank=True)

    resultado_input_5 = models.DecimalField(
        max_digits=7,
        decimal_places=3,
        default=0.0,
        blank=True)

    resultado_fback_1 = models.DecimalField(
        default=0.0,
        max_digits=7,
        decimal_places=3,
        null=True)

    resultado_fback_2 = models.DecimalField(
        default=0.0,
        max_digits=7,
        decimal_places=3,
        null=True)

    resultado_fback_3 = models.DecimalField(
        default=0.0,
        max_digits=7,
        decimal_places=3,
        null=True)

    resultado_fback_4 = models.DecimalField(
        default=0.0,
        max_digits=7,
        decimal_places=3,
        null=True)

    resultado_fback_5 = models.DecimalField(
        default=0.0,
        max_digits=7,
        decimal_places=3,
        null=True)

    resultado_nota_1 = models.DecimalField(
        max_digits=7,
        decimal_places=3,
        default=0.0,
        blank=True)

    resultado_nota_2 = models.DecimalField(
        max_digits=7,
        decimal_places=3,
        default=0.0,
        blank=True)

    resultado_nota_3 = models.DecimalField(
        max_digits=7,
        decimal_places=3,
        default=0.0,
        blank=True)

    resultado_nota_4 = models.DecimalField(
        max_digits=7,
        decimal_places=3,
        default=0.0,
        blank=True)

    resultado_nota_5 = models.DecimalField(
        max_digits=7,
        decimal_places=3,
        default=0.0,
        blank=True)

    nota_resultado = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.0,
        blank=True)

    projeto = models.OneToOneField(Projeto, on_delete=models.CASCADE)

    resultado_consideracao_1 = models.CharField(max_length=255, null=True, blank=True)
    resultado_consideracao_2 = models.CharField(max_length=255, null=True, blank=True)
    resultado_consideracao_3 = models.CharField(max_length=255, null=True, blank=True)
    resultado_consideracao_4 = models.CharField(max_length=255, null=True, blank=True)
    resultado_consideracao_5 = models.CharField(max_length=255, null=True, blank=True)

    def setNotaResultado(self):
        data = float(self.projeto.modelo.resultado_peso_1)*float(self.resultado_nota_1)
        data += float(self.projeto.modelo.resultado_peso_2)*float(self.resultado_nota_2)
        data += float(self.projeto.modelo.resultado_peso_3)*float(self.resultado_nota_3)
        data += float(self.projeto.modelo.resultado_peso_4)*float(self.resultado_nota_4)
        data += float(self.projeto.modelo.resultado_peso_5)*float(self.resultado_nota_5)
        data = data*float(self.projeto.modelo.resultado_peso)
        return data

class Apresentacao(models.Model):

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    inscricao = models.OneToOneField(Inscricao, on_delete=models.CASCADE)
    modelo = models.ForeignKey(ProjetoModelo, on_delete=models.PROTECT)

    apresentacao_nota_1 = models.DecimalField(max_digits=7, decimal_places=3, default=0.0, blank=True)
    apresentacao_nota_2 = models.DecimalField(max_digits=7, decimal_places=3, default=0.0, blank=True)
    apresentacao_nota_3 = models.DecimalField(max_digits=7, decimal_places=3, default=0.0, blank=True)
    apresentacao_nota_4 = models.DecimalField(max_digits=7, decimal_places=3, default=0.0, blank=True)
    apresentacao_nota_5 = models.DecimalField(max_digits=7, decimal_places=3, default=0.0, blank=True)
    apresentacao_consideracao_1 = models.CharField(max_length=255, null=True, blank=True)
    apresentacao_consideracao_2 = models.CharField(max_length=255, null=True, blank=True)
    apresentacao_consideracao_3 = models.CharField(max_length=255, null=True, blank=True)
    apresentacao_consideracao_4 = models.CharField(max_length=255, null=True, blank=True)
    apresentacao_consideracao_5 = models.CharField(max_length=255, null=True, blank=True)

    nota_apresentacao = models.DecimalField(max_digits=7, decimal_places=3, default=0.0, blank=True)

    def setNotaApresentacao(self):
        data = float(self.modelo.apresentacao_peso_1)*float(self.apresentacao_nota_1)
        data += float(self.modelo.apresentacao_peso_2)*float(self.apresentacao_nota_2)
        data += float(self.modelo.apresentacao_peso_3)*float(self.apresentacao_nota_3)
        data += float(self.modelo.apresentacao_peso_4)*float(self.apresentacao_nota_4)
        data += float(self.modelo.apresentacao_peso_5)*float(self.apresentacao_nota_5)
        data = data*float(self.modelo.apresentacao_peso)
        return data

class Extra(models.Model):

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    nota_extra = models.DecimalField(max_digits=6, decimal_places=3, default=0.0, blank=True)
    penalidade_nota = models.DecimalField(max_digits=6, decimal_places=3, default=0, blank=True)
    divulgacao_nota = models.DecimalField(max_digits=6, decimal_places=3, default=0, blank=True)
    penalidade_consideracao = models.CharField(max_length=255, null=True, blank=True)
    divulgacao_consideracao = models.CharField(max_length=255, null=True, blank=True)

    inscricao = models.OneToOneField(Inscricao, on_delete=models.CASCADE)

    def setNotaExtra(self):
        data = self.penalidade_nota+self.divulgacao_nota
        return data

class Bibliografia(models.Model):

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    arquivo = models.FileField(upload_to='pdf/%Y/%m/%d/', null=True)
    bibliografia_qde = models.IntegerField(null=True, blank=True)
    consideracoes = models.CharField(max_length=255, null=True, blank=True)
    nota_bibliografia = models.DecimalField(max_digits=6, decimal_places=3, default=0.0, blank=True)

    inscricao = models.OneToOneField(Inscricao, on_delete=models.CASCADE)
    modelo = models.ForeignKey(ProjetoModelo, on_delete=models.PROTECT)

    def setNotaBibliografia(self):
        data = 0.0
        try:
            data = float(self.bibliografia_qde)/float(self.modelo.bibliografia_total)
            data = data*float(self.modelo.bibliografia_peso)
        except:
            self.modelo.bibliografia_total = 0
        return data

class Proposta(models.Model):

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    consideracoes = models.CharField(max_length=255, null=True, blank=True, default='A proposta atende os objetivos da chamada.')
    nota_proposta = models.DecimalField(max_digits=6, decimal_places=3, default=0.0, blank=True)
    conteudo = models.TextField(null=True)
    proposta_status = models.CharField(
        max_length=3,
        default="sim",
        choices=(("sim", "Sim"), ("nao", "Não"))
        )

    inscricao = models.OneToOneField(Inscricao, on_delete=models.CASCADE)
    modelo = models.ForeignKey(ProjetoModelo, on_delete=models.PROTECT)

    def setNotaProposta(self):
        if self.proposta_status == 'sim':
            data = self.modelo.proposta_peso
        elif self.proposta_status == 'nao':
            data = 0.0
        return data

class Financeiro(models.Model):

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    comprovante_1 = models.FileField(upload_to='pdf/%Y/%m/%d/', null=True)
    comprovante_2 = models.FileField(upload_to='pdf/%Y/%m/%d/', null=True)
    comprovante_3 = models.FileField(upload_to='pdf/%Y/%m/%d/', null=True)

    consideracoes = models.CharField(max_length=255, null=True, blank=True, default='Aguarde')

    financeiro_status = models.CharField(
        max_length=10,
        default="Adimplente",
        choices=(("adimplente", "Adimplente"), ("em_debito", "Em débito"))
        )

    inscricao = models.OneToOneField(Inscricao, on_delete=models.CASCADE)
