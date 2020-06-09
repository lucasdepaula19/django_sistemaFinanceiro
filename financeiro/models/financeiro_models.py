from django.db import models
from django.apps import apps

# Create your models here.

class ClassContasReceber(models.Model):
	descricao = models.CharField(max_length=200)
	
	def __str__(self):
		detalhe = f""" Descrição: {self.descricao}"""
		return detalhe

class ClassContasPagar(models.Model):
	descricao = models.CharField(max_length=200)
	
	def __str__(self):
		detalhe = f""" Descrição: {self.descricao}"""
		return detalhe

class FormaPagamentoRecebimento(models.Model):
	descricao = models.CharField(max_length=200)
	
	def __str__(self):
		detalhe = f""" Descrição: {self.descricao}"""
		return detalhe

class Situacao(models.Model):
	status = models.CharField(max_length=200)
	
	def __str__(self):
		detalhe = f""" status: {self.status}"""
		return detalhe

class ContasPagar(models.Model):
	descricao = models.CharField(max_length=200)
	data_vencimento = models.DateField(null=True)
	data_pagamento = models.DateField(null=True)
	valor = models.IntegerField(default=0)
	classificacao = models.ForeignKey("ClassContasPagar", on_delete=models.CASCADE)
	forma_pagamento = models.ForeignKey("FormaPagamentoRecebimento", on_delete=models.CASCADE)
	situacao = models.ForeignKey("Situacao", on_delete=models.CASCADE)

	def __str__(self):
		detalhe = f""" Descrição: {self.descricao}, Data de vencimento: {self.data_vencimento}, 
        Data de Pagamento: {self.data_pagamento}, Valor: {self.valor}, Classificação: {self.classificacao}, 
        Forma de pagamento: {self.forma_pagamento}, Situação: {self.situacao}"""
		return detalhe

class ContasReceber(models.Model):
	descricao = models.CharField(max_length=200)
	data_expectativa = models.DateField(null=True)
	data_recebimento = models.DateField(null=True)
	valor = models.IntegerField(default=0)
	classificacao = models.ForeignKey("ClassContasReceber", on_delete=models.CASCADE)
	forma_recebimento = models.ForeignKey("FormaPagamentoRecebimento", on_delete=models.CASCADE)
	situacao = models.ForeignKey("Situacao", on_delete=models.CASCADE)

	def __str__(self):
		detalhe = f""" Descrição: {self.descricao}, Data de expectativa: {self.data_expectativa}, 
        Data de Vencimento: {self.data_recebimento}, Valor: {self.valor}, Classificação: {self.classificacao}, 
        Forma de recebimento: {self.forma_recebimento}, Situação: {self.situacao}"""
		return detalhe