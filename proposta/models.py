from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Sum,Avg
from localflavor.br.br_states import STATE_CHOICES
from django.utils.safestring import mark_safe
from django.contrib.admin.views.main import ChangeList

# Create your models here.

class Cliente(models.Model):
	nome = models.CharField(max_length=100)

	def __str__(self):
		return self.nome
		
class Proposta(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	cpf = models.CharField(blank=True, max_length=14)
	cnpj = models.CharField(blank=True, max_length=18)
	endereco = models.CharField(blank=True, max_length=200)
	bairro = models.CharField(blank=True, max_length=100)
	cidade = models.CharField(blank=True, max_length=100)
	estado = models.CharField(max_length=2, null=True, blank=True, choices=STATE_CHOICES)
	data = models.DateField('Data de Emissão' )
	VALIDADE_CHOICES = (
		('Quinze','15 (Quinze)'),
		('Trinta','30 (Trinta)'),
		('Sessenta','60 (Sessenta)'),
		)

	validade = models.CharField(blank=True, max_length=200, choices = VALIDADE_CHOICES) 
	valor = models.DecimalField(max_digits=8, decimal_places=2)
	CATEGORY_CHOICES = (
			('Atrasado','Atrasado'),
			('AVencer','Á Vencer'),
			('Pago','Pago'),
			)

	situacao = models.CharField(max_length=200, choices = CATEGORY_CHOICES)
	pago = models.BooleanField(default=False)

	dominio = models.CharField(blank=True, max_length=200, help_text='URL - exe: seudominio.com.br')
	dominio_loguin = models.CharField(max_length=200, blank=True, help_text='URL - exe: seudominio.com.br/admin')
	loguin = models.CharField(max_length=30, blank=True)
	senha = models.CharField(max_length=30, blank=True)

	def imprimir(self):
			return mark_safe("""<a href=\"/proposta/%s/\" target="_blank"><img src=\"/static/images/b_print.png\"></a>""" % self.id)


	class Meta:
		ordering = ['-data']
		verbose_name = 'UMA PROPOSTA'
		verbose_name_plural = 'PROPOSTAS'

	def __str__(self):
		if self.cliente.nome:
			return self.cliente.nome
		else:
			return self.custom_alias_name