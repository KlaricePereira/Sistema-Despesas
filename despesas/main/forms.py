from django import forms
from .models import Saida, Entrada, Nota

class SaidaForm(forms.ModelForm):
    class Meta:
        model = Saida
        fields = ['descricao', 'data', 'valor']
        
class EntradaForm(forms.ModelForm):
   class Meta:
       model = Entrada
       fields = ['descricao', 'data', 'valor']
       
class HistoricoForm(forms.Form):
  entrada_form = EntradaForm()
  saida_form = SaidaForm()
  
class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['titulo', 'conteudo']
        
        

class FiltroForm(forms.Form):
    MES_CHOICES = [
        (1, 'Janeiro'),
        (2, 'Fevereiro'),
        (3, 'Março'),
        (4, 'Abril'),
        (5, 'Maio'),
        (6, 'Junho'),
        (7, 'Julho'),
        (8, 'Agosto'),
        (9, 'Setembro'),
        (10, 'Outubro'),
        (11, 'Novembro'),
        (12, 'Dezembro'),
    ]

    mes = forms.ChoiceField(choices=MES_CHOICES, label='Mês')
    ano = forms.IntegerField(required=False, label="Ano", widget=forms.NumberInput(attrs={'placeholder': 'Ano'}))
  
