from django import forms
from .models import ClassContasReceber, ClassContasPagar, FormaPagamentoRecebimento, Situacao, ContasPagar, ContasReceber

class ClassContasReceberForm(forms.ModelForm):
    class Meta:
        model = ClassContasReceber
        fields = ['descricao']

class ClassContasPagarForm(forms.ModelForm):
    class Meta:
        model = ClassContasPagar
        fields = ['descricao']

class FormaPagamentoRecebimentoForm(forms.ModelForm):
    class Meta:
        model = FormaPagamentoRecebimento
        fields = ['descricao']

class ContasPagarForm(forms.ModelForm):
    class Meta:
        model = ContasPagar
        fields = ['descricao','data_vencimento', 'data_pagamento', 'valor','classificacao', 'forma_pagamento', 'situacao']

class ContasReceberForm(forms.ModelForm):
    class Meta:
        model = ContasReceber
        fields = ['descricao','data_expectativa', 'data_recebimento', 'valor','classificacao', 'forma_recebimento', 'situacao']