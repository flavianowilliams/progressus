from chamadas.models import Inscricao

class Valor():

    def __init__(self, args):

        self.args = args

        object_list = Inscricao.objects.all()

        if self.args['atributo'] == 'resultado_fback_1':
            lista = [object.projeto.resultado.resultado_fback_1 for object in object_list if object.tema == self.args['tema']]
        elif self.args['atributo'] == 'resultado_fback_2':
            lista = [object.projeto.resultado.resultado_fback_2 for object in object_list if object.tema == self.args['tema']]
        elif self.args['atributo'] == 'resultado_fback_3':
            lista = [object.projeto.resultado.resultado_fback_3 for object in object_list if object.tema == self.args['tema']]
        elif self.args['atributo'] == 'resultado_fback_4':
            lista = [object.projeto.resultado.resultado_fback_4 for object in object_list if object.tema == self.args['tema']]
        elif self.args['atributo'] == 'resultado_fback_5':
            lista = [object.projeto.resultado.resultado_fback_5 for object in object_list if object.tema == self.args['tema']]

        self.lista = lista

    def setValor(self):

        if self.args['regra'] == 'direta':
            nota_min = min(self.lista)
            nota_max = max(self.lista)
        elif self.args['regra'] == 'inversa':
            nota_min = max(self.lista)
            nota_max = min(self.lista)

        if abs(nota_max-nota_min) < 1.e-4:
            nota = 100*(self.args['valor']-nota_max)/(nota_max-nota_min)
        else:
            nota = 0.0

        return nota
