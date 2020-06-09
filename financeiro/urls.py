from django.urls import path

from .views import financeiro_views as fv

urlpatterns = [
	path('', fv.home, name="index"),
    path('criarClassContasReceber/', fv.criar_classContasReceber, name="criar_classContasReceber"),
]