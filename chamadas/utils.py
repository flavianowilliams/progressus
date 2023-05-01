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

        nota = 100*(self.args['valor']-nota_max)/(nota_max-nota_min)

        return nota

#    def setValor(self):
#
#        if self.args['regra'] == 'direta':
#
#            maximo = max(self.lista)
#            if maximo == 0.0:
#                if self.args['valor'] == 0.0:
#                    nota = 0.0
#                else:
#                    nota = 100.0
#            else:
#                nota = 100*float(self.args['valor'])/float(maximo)
#
#        elif self.args['regra'] == 'inversa':
#
#            minimo = min(self.lista)
#            if minimo == 0.0:
#                if self.args['valor'] == 0.0:
#                    nota = 100.0
#                else:
#                    nota = 0.0
#            else:
#                nota = 100*float(minimo)/float(self.args['valor'])
#
#        return nota
