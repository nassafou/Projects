# Create your views here. 
#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  text = """<h1>Bienvenue sur mon Blog !</h1>
<p> Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
  return HttpResponse(text)

