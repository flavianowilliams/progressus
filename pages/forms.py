from django import forms
from .models import Noticia

class NoticiaFormCreate(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = [
            'titulo',
            'texto',
            'link',
            'imagem',
                ]

    def clean_titulo(self):
        data = self.cleaned_data['titulo']
        if Noticia.objects.filter(titulo = data).exists():
            raise forms.ValidationError('O título {} já está em uso.'.format(data))
        return data

class NoticiaFormUpdate(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = [
            'titulo',
            'texto',
            'link',
            'imagem',
                ]
