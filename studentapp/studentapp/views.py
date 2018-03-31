import random

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def test(r: HttpRequest):
    return HttpResponse("hi")


def index(r: HttpRequest):
    template = 'index.html'
    context = {}

    nums = [random.randrange(0, 10) for _ in range(10)]

    context['test'] = nums

    return render(r, template, context)
