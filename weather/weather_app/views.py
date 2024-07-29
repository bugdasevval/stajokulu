from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('anasayfa')

def detay(request):
    return HttpResponse('detay')


def 