from django.urls import path

from .views import financeiro_views as fv

urlpatterns = [
	path('', fv.home, name="index"),
    path('criarClassContasReceber/', fv.criar_classContasReceber, name="criar_classContasReceber"),
    path('criarClassContasPagar/', fv.criar_classContasPagar, name="criar_classContasPagar"),
    path('criarFormaPagamentoRecebimento/', fv.criar_formaPagamentoRecebimento, name="criar_formaPagamentoRecebimento"),
    path('criarContasPagar/', fv.criar_ContasPagar, name="criar_ContasPagar"),
    path('criarContasReceber/', fv.criar_contasReceber, name="criar_contasReceber"),

    path('listarClassContasReceber/', fv.listar_classContasReceber, name="listar_classContasReceber"),
    path('listarClassContasPagar/', fv.listar_classContasPagar, name="listar_classContasPagar"),
    path('listarFormaPagamentoRecebimento/', fv.listar_formaPagamentoRecebimento, name="listar_formaPagamentoRecebimento"),
    path('listarContasPagar/', fv.listar_ContasPagar, name="listar_ContasPagar"),
    path('listarContasReceber/', fv.listar_contasReceber, name="listar_contasReceber"),

    path('excluirClassContasReceber/<int:id_item>/', fv.excluir_classContasReceber, name="excluir_classContasReceber"),
    path('excluirClassContasPagar/<int:id_item>/', fv.excluir_classContasPagar, name="excluir_classContasPagar"),
    path('excluirFormaPagamentoRecebimento/<int:id_item>/', fv.excluir_formaPagamentoRecebimento, name="excluir_formaPagamentoRecebimento"),
    path('excluirContasPagar/<int:id_item>/', fv.excluir_contasPagar, name="excluir_contasPagar"),
    path('excluirContasReceber/<int:id_item>/', fv.excluir_contasReceber, name="excluir_contasReceber"),

    path('listarContasPagar/filterPagar/', fv.filter_pagar, name="filter_pagar"),
    path('listarContasReceber/filterReceber/', fv.filter_receber, name="filter_receber"),
]