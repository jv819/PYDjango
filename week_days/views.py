from django.shortcuts import render
from django.http import HttpResponse


def monday(request):
    return HttpResponse("Дела на понедельник")


def tuesday(request):
    return HttpResponse("Дела на вторник")
