from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from django.shortcuts import render
from datetime import datetime
from ..models import ClassContasReceber, ClassContasPagar, FormaPagamentoRecebimento, Situacao, ContasPagar, ContasReceber
from ..forms import ClassContasReceberForm, ClassContasPagarForm, FormaPagamentoRecebimentoForm, ContasPagarForm, ContasReceberForm

# Create your views here.
@csrf_exempt
@require_http_methods(["GET","POST"])
def home(request):
	template = loader.get_template('index.html')
	context = {
	}
	return HttpResponse(template.render(context, request))

@csrf_exempt
@require_http_methods(["POST","GET"])
def criar_classContasReceber(request):
	form2 = ClassContasReceberForm(request.POST or None)

	context = {
		'form': ClassContasReceberForm(request.POST or None),
	}

	if(form2.is_valid()):
		form2.save()
		return redirect('/financeiro')

	template = loader.get_template('classContasReceber.html')
	return HttpResponse(template.render(context, request))

@csrf_exempt
@require_http_methods(["POST","GET"])
def criar_classContasPagar(request):
	form2 = ClassContasPagarForm(request.POST or None)

	context = {
		'form': ClassContasPagarForm(request.POST or None),
	}

	if(form2.is_valid()):
		form2.save()
		return redirect('/financeiro')

	template = loader.get_template('classContasPagar.html')
	return HttpResponse(template.render(context, request))

@csrf_exempt
@require_http_methods(["POST","GET"])
def criar_formaPagamentoRecebimento(request):
	form2 = FormaPagamentoRecebimentoForm(request.POST or None)

	context = {
		'form': FormaPagamentoRecebimentoForm(request.POST or None),
	}

	if(form2.is_valid()):
		form2.save()
		return redirect('/financeiro')

	template = loader.get_template('formaPagamentoRecebimento.html')
	return HttpResponse(template.render(context, request))

@csrf_exempt
@require_http_methods(["POST","GET"])
def criar_ContasPagar(request):
	form2 = ContasPagarForm(request.POST or None)

	context = {
		'form': ContasPagarForm(request.POST or None),
	}

	if(form2.is_valid()):
		form2.save()
		return redirect('/financeiro')

	template = loader.get_template('contasPagar.html')
	return HttpResponse(template.render(context, request))

@csrf_exempt
@require_http_methods(["POST","GET"])
def criar_contasReceber(request):
	form2 = ContasReceberForm(request.POST or None)

	context = {
		'form': ContasReceberForm(request.POST or None),
	}

	if(form2.is_valid()):
		form2.save()
		return redirect('/financeiro')

	template = loader.get_template('contasReceber.html')
	return HttpResponse(template.render(context, request))

@csrf_exempt
@require_http_methods(["POST","GET"])
def listar_classContasReceber(request):
	result = ClassContasReceber.objects.all()
	template = loader.get_template('listarClassContasReceber.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

@csrf_exempt
@require_http_methods(["POST","GET"])
def listar_classContasPagar(request):
	result = ClassContasPagar.objects.all()
	template = loader.get_template('listarClassContasPagar.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

@csrf_exempt
@require_http_methods(["POST","GET"])
def listar_formaPagamentoRecebimento(request):
	result = FormaPagamentoRecebimento.objects.all()
	template = loader.get_template('listarFormaPagamentoRecebimento.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

@csrf_exempt
@require_http_methods(["POST","GET"])
def listar_ContasPagar(request):
	result = ContasPagar.objects.all()
	template = loader.get_template('listarContasPagar.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

@csrf_exempt
@require_http_methods(["POST","GET"])
def listar_contasReceber(request):
	result = ContasReceber.objects.all()
	template = loader.get_template('listarContasReceber.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

def excluir_classContasReceber(request, id_item):
	try:
		item = ClassContasReceber.objects.get(id=id_item)
		item.delete()		
		return HttpResponse(f"Excluiu {item.descricao} (id={item.id})")
	except ObjectDoesNotExist:
		return HttpResponse("Item não encontrado")

def excluir_classContasPagar(request, id_item):
	try:
		item = ClassContasPagar.objects.get(id=id_item)
		item.delete()		
		return HttpResponse(f"Excluiu {item.descricao} (id={item.id})")
	except ObjectDoesNotExist:
		return HttpResponse("Item não encontrado")
	
def excluir_formaPagamentoRecebimento(request, id_item):
	try:
		item = FormaPagamentoRecebimento.objects.get(id=id_item)
		item.delete()		
		return HttpResponse(f"Excluiu {item.descricao} (id={item.id})")
	except ObjectDoesNotExist:
		return HttpResponse("Item não encontrado")

def excluir_contasPagar(request, id_item):
	try:
		item = ContasPagar.objects.get(id=id_item)
		item.delete()		
		return HttpResponse(f"Excluiu {item.descricao} (id={item.id})")
	except ObjectDoesNotExist:
		return HttpResponse("Item não encontrado")

def excluir_contasReceber(request, id_item):
	try:
		item = ContasReceber.objects.get(id=id_item)
		item.delete()		
		return HttpResponse(f"Excluiu {item.descricao} (id={item.id})")
	except ObjectDoesNotExist:
		return HttpResponse("Item não encontrado")