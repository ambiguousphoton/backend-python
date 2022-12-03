from django.shortcuts import render
from django.http import HttpResponse
from .models import Todolist, Item

def index (response, id):
    ls = Todolist.objects.get(id = id)
    return HttpResponse("<h1>%s</h1>" %ls.name)



# def v1(response):
#     return HttpResponse("<button> <h5> jai ho</h5> </button>")