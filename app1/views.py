from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def a1_dhoni(request):
    return HttpResponse('Dhoni is best wicketkeeper')