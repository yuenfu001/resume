from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hmm(request):
    return HttpResponse("This is app for cataloging")
