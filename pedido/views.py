from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView


class Pagar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Pagar')


class FecharPedido(View):
    def get(self, *args, **kwargs):
        return HttpResponse('FecharPedido')


class Detalhe(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe')
