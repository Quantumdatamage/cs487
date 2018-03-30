from django.http import HttpRequest, HttpResponse


def test(r: HttpRequest):
    return HttpResponse("hi")
