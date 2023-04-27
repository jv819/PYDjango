from django.shortcuts import render
from django.http import HttpResponse


def aries(request):
    return HttpResponse("знак зодиака овен")


def taurus(request):
    return HttpResponse("знак зодиака телец")


def gemini(request):
    return HttpResponse("знак зодиака близнецы")


def cancer(request):
    return HttpResponse("знак зодиака рак")


def leo(request):
    return HttpResponse("знак зодиака лев")


def virgo(request):
    return HttpResponse("знак зодиака дева")


def libra(request):
    return HttpResponse("Знак зодиака весы")


def scorpion(request):
    return HttpResponse("Знак зодиака скорпион")


def sagittarius(request):
    return HttpResponse("знак зодиака стрелец")


def capricorn(request):
    return HttpResponse("знак зодиака козерог")


def aquarius(request):
    return HttpResponse("знак зодиака водолей")


def pisces(request):
    return HttpResponse("знак зодиака рыбы")
