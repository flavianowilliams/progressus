from chamadas.models import Inscricao

class Valor():

    def __init__(self, kwargs):

        self.kwargs = kwargs

        object_list = Inscricao.objects.all()

        if self.kwargs['atributo'] == 'resultado_fback_1':
            lista = [object.projeto.resultado.resultado_fback_1 for object in object_list if object.tema == self.kwargs['tema']]
        elif self.kwargs['atributo'] == 'resultado_fback_2':
            lista = [object.projeto.resultado.resultado_fback_2 for object in object_list if object.tema == self.kwargs['tema']]
        elif self.kwargs['atributo'] == 'resultado_fback_3':
            lista = [object.projeto.resultado.resultado_fback_3 for object in object_list if object.tema == self.kwargs['tema']]
        elif self.args['atributo'] == 'resultado_fback_4':
            lista = [object.projeto.resultado.resultado_fback_4 for object in object_list if object.tema == self.kwargs['tema']]
        elif self.kwargs['atributo'] == 'resultado_fback_5':
            lista = [object.projeto.resultado.resultado_fback_5 for object in object_list if object.tema == self.kwargs['tema']]

        self.lista = lista

    def setValor(self):

#        if self.args['regra'] == 'direta':
#            x1 = min(self.lista)
#            x2 = max(self.lista)
#        elif self.args['regra'] == 'inversa':
#            x1 = max(self.lista)
#            x2 = min(self.lista)

#        if abs(x2-x1) > 1.e-4:
#            nota = 100*(self.args['valor']-x1)/(x2-x1)
#        else:
#            nota = 0.0

        nota = 100

        return nota
