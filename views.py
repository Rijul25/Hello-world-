# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    response = HttpResponse("Hello world !")

    return response
def check(request):
    return HttpResponse("<h1>Hello rijul kaisa he </h1>")