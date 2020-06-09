from django.urls import path

from .views import financeiro_views as fv

urlpatterns = [
	path('', fv.home, name="index"),
    path('criarClassContasReceber/', fv.criar_classContasReceber, name="criar_classContasReceber"),
    path('criarClassContasPagar/', fv.criar_classContasPagar, name="criar_classContasPagar"),
    path('criarFormaPagamentoRecebimento/', fv.criar_formaPagamentoRecebimento, name="criar_formaPagamentoRecebimento"),
    path('criarContasPagar/', fv.criar_ContasPagar, name="criar_ContasPagar"),
    path('criarContasReceber/', fv.criar_contasReceber, name="criar_contasReceber"),
]