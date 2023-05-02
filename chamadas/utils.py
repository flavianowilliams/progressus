from chamadas.models import Resultado, Chamada

class Valor():

    def __init__(self, kwargs):

        self.kwargs = kwargs

        chamada = Chamada.objects.get(pk = kwargs['pk'])

        object_list = [object for object in Resultado.objects.all() if object.projeto.inscricao.chamada == chamada and object.projeto.inscricao.tema == self.kwargs['tema']]

        if self.kwargs['atributo'] == 'resultado_fback_1':
            lista = [object.resultado_fback_1 for object in object_list if object.resultado_fback_1 > 1.e-8]
#        elif self.kwargs['atributo'] == 'resultado_fback_2':
#            lista = [object.projeto.resultado.resultado_fback_2 for object in object_list if object.tema == self.kwargs['tema']]
#        elif self.kwargs['atributo'] == 'resultado_fback_3':
#            lista = [object.projeto.resultado.resultado_fback_3 for object in object_list if object.tema == self.kwargs['tema']]
#        elif self.args['atributo'] == 'resultado_fback_4':
#            lista = [object.projeto.resultado.resultado_fback_4 for object in object_list if object.tema == self.kwargs['tema']]
#        elif self.kwargs['atributo'] == 'resultado_fback_5':
#            lista = [object.projeto.resultado.resultado_fback_5 for object in object_list if object.tema == self.kwargs['tema']]

        self.lista = lista

    def setValor(self):

        if self.kwargs['regra'] == 'direta':
            x1 = min(self.lista)
            x2 = max(self.lista)
        elif self.kwargs['regra'] == 'Inversa':
            x1 = max(self.lista)
            x2 = min(self.lista)

        if abs(x2-x1) > 1.e-8:
            nota = 100*(self.kwargs['valor']-x1)/(x2-x1)
            if self.kwargs['valor'] < 1.e-8:
                nota = 0.0
        else:
            nota = 0.0

        return nota
