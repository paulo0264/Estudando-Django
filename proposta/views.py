from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from proposta.models import Cliente, Proposta

# Home

def home(requests):
	return render(requests, "home.html")

