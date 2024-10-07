from django.http import HttpResponse

def home(request):
    return HttpResponse("This Is home Page")

def about(request):
    return HttpResponse("This Is about Page")