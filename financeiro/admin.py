from django.contrib import admin

# Register your models here.
from .models import ClassContasReceber, ClassContasPagar, FormaPagamentoRecebimento, Situacao, ContasPagar, ContasReceber

admin.site.register(ClassContasReceber)
admin.site.register(ClassContasPagar)
admin.site.register(FormaPagamentoRecebimento)
admin.site.register(Situacao)
admin.site.register(ContasPagar)
admin.site.register(ContasReceber)