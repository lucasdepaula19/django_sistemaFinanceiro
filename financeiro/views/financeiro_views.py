from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from django.shortcuts import render
from datetime import datetime
#from ..models import Class 
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